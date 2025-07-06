import random
from datetime import datetime, timedelta

class ShoppingCart:

    def __init__(self):
        self.catalog = [
            ["101", "Laptop", 60000, 5, "physical", 2.5],
            ["102", "E-Book", 100, 100, "digital", "downloadlink.com/book"],
            ["103", "Pen", 5, 200, "generic"],
            ["104", "White Sneaker", 2500, 10, "physical",1.1],
            ["105", "Kurkure", 20, 50, "physical",0.1]
        ]
        self.items = []

    def view_available_products(self):
        print("Available Products:\n")
        for product in self.catalog:
            if product[3] > 0:  
                product_id = product[0]
                name = product[1]
                price = product[2]
                quantity = product[3]
                ptype = product[4]
                if ptype == "physical":
                    weight = product[5]
                    print(f"ID: {product_id}, Name: {name}, Price: ₹{price:.2f}, Stock: {quantity}, Weight: {weight}kg")
                elif ptype == "digital":
                    download_link = product[5]
                    print(f"ID: {product_id}, Name: {name}, Price: ₹{price:.2f}, Stock: {quantity}, Download: {download_link}")
                else:
                    print(f"ID: {product_id}, Name: {name}, Price: ₹{price:.2f}, Stock: {quantity}")

    def add_to_cart(self):
        product_id = input("Enter product ID to add to cart: ")
        try:
            quantity = int(input("Enter quantity to add: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            return
        for product in self.catalog:
            if product[0] == product_id:
                if product[3] >= quantity:
                    product[3] -= quantity  
                    name = product[1]
                    price = product[2]
                    subtotal = price * quantity
                    for item in self.items:
                        if item[0] == product_id:
                            item[3] += quantity
                            item[4] = item[2] * item[3]
                            print(f"Updated quantity of '{name}' in cart.")
                            return            
                    self.items.append([product_id, name, price, quantity, subtotal])
                    print(f"'{name}' added to cart.")
                    return
                else:
                    print("Not enough stock.")
                    return
        print("Product ID not found in catalog.")

    def update_cart_quantity(self):    
        product_id = input("Enter the product ID you want to update in the cart: ")   
        found = False
        for item in self.items:
            if item[0] == product_id:
                found = True
                current_quantity = item[3]
                print(f"Current quantity of '{item[1]}' in cart is {current_quantity}")            
                try:
                    new_quantity = int(input("Enter the new quantity: "))
                    if new_quantity < 0:
                        print("Quantity cannot be negative.")
                        return
                    quantity_difference = new_quantity - current_quantity
                    for product in self.catalog:
                        if product[0] == product_id:
                            stock_available = product[3]
                            if quantity_difference > 0:
                                if stock_available >= quantity_difference:
                                    product[3] -= quantity_difference
                                    item[3] = new_quantity
                                    item[4] = item[2] * new_quantity
                                    print(f"Quantity updated to {new_quantity}.")
                                else:
                                    print("Not enough stock available to increase quantity.")
                            elif quantity_difference < 0:
                                product[3] += abs(quantity_difference)
                                item[3] = new_quantity
                                item[4] = item[2] * new_quantity
                                print(f"Quantity reduced to {new_quantity}.")
                            else:
                                print("Quantity is unchanged.")
                            return
                except ValueError:
                    print("Please enter a valid number.")
                    return
        if not found:
            print("Product ID not found in the cart.")

    def remove_item_from_cart(self): 
        product_id = input("Enter the product ID to remove from the cart: ")
        item_found = False
        for item in self.items:
            if item[0] == product_id:
                item_found = True
                quantity_in_cart = item[3]
                for product in self.catalog:
                    if product[0] == product_id:
                        product[3] += quantity_in_cart  
                self.items.remove(item)
                print(f"Item '{item[1]}' removed from the cart.")
                return  
        if not item_found:
            print("Product ID not found in the cart.")

    def view_cart_contents(self):
        if len(self.items) == 0:
            print("Your cart is currently empty.")
            return
        print("Your Shopping Cart:")
        print("-" * 50)
        grand_total = 0  
        for item in self.items:
            product_id = item[0]
            name = item[1]
            unit_price = item[2]
            quantity = item[3]
            subtotal = item[4]
            grand_total += subtotal
            print(f"Product ID: {product_id}")
            print(f"Name: {name}")
            print(f"Unit Price: ₹{unit_price:.2f}")
            print(f"Quantity: {quantity}")
            print(f"Subtotal: ₹{subtotal:.2f}")
            print("-" * 50)
        delivery_charge = 0
        if grand_total < 500:
            delivery_charge = 100
            print(f"Delivery Charge: ₹{delivery_charge:.2f} (Added for orders below ₹500)")
        final_total = grand_total + delivery_charge
        print(f"Total Amount Payable: ₹{final_total:.2f}")

    def get_expected_delivery_date(self):
        delivery_days = random.randint(3, 5)
        today = datetime.now()
        expected_date = today + timedelta(days=delivery_days)
        formatted_date = expected_date.strftime("%d %B %Y")
        print(f"Your expected delivery date is: {formatted_date}")

    def empty_cart(self):
        if len(self.items) == 0:
            print("Cart is already empty.")
            return
        confirm = input("Are you sure you want to remove all items from the cart? (y/n): ").lower()
        if confirm != 'y':
            print("Cart was not emptied.")
            return
        for item in self.items:
            product_id = item[0]
            quantity_in_cart = item[3]
            for product in self.catalog:
                if product[0] == product_id:
                    product[3] += quantity_in_cart  
        self.items.clear()
        print("All items have been removed from the cart.")

    def run(self):
        while True:
            print("\n========== ONLINE SHOPPING CART ==========")
            print("1. View Available Products")
            print("2. Add Existing Product to Cart")
            print("3. Update Quantity of Item in Cart")
            print("4. Remove Item from Cart")
            print("5. View Cart Contents")
            print("6. View Expected Delivery Date")
            print("7. Empty Entire Cart")
            print("8. Exit")
            print("==========================================")
            choice = input("Enter your choice (1-8): ")
            if choice == '1':
                self.view_available_products()
            elif choice == '2':
                self.add_to_cart()
            elif choice == '3':
                self.update_cart_quantity()
            elif choice == '4':
                self.remove_item_from_cart()
            elif choice == '5':
                self.view_cart_contents()
            elif choice == '6':
                self.get_expected_delivery_date()
            elif choice == '7':
                self.empty_cart()
            elif choice == '8':
                print("Thank you for using the shopping cart!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == '__main__':
    cart = ShoppingCart()
    cart.run()
