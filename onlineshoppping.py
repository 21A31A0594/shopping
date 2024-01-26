class Product:
    def __init__(self, prod_id, prod_name, prod_price, prod_quantity):
        self.prod_id = prod_id
        self.name = prod_name
        self.price = prod_price
        self.stock = prod_quantity

    def __str__(self):
        return f"{self.name}, Price: ${self.price}, Stock: {self.stock}"

class Shopping:
    def __init__(self):
        self.items = {}

    def add_prod(self, product, quantity):
        if product.prod_id not in self.items:
            self.items[product.prod_id] = {'product': product, 'quantity': 0}

        if 0 < quantity <= product.stock:
            self.items[product.prod_id]['quantity'] += quantity
            product.stock -= quantity
            print(f"{product.name} has been added.")
        else:
            print("Insufficient quantity.")

    def remove_product(self, product, quantity):
        if product.prod_id in self.items and quantity > 0:
            if quantity <= self.items[product.prod_id]['quantity']:
                self.items[product.prod_id]['quantity'] -= quantity
                product.stock += quantity
                print(f"{quantity} {product.name}(s) removed from the cart.")
            else:
                print("Invalid quantity.")
            if self.items[product.prod_id]['quantity'] == 0:
                del self.items[product.prod_id]
        else:
            print(f"{product.name} not found in the cart.")

    def check_cart(self):
        if not self.items:
            print("No products in the cart.")
        else:
            total = 0
            for item in self.items.values():
                product = item['product']
                quantity = item['quantity']
                item_price = quantity * product.price
                total += item_price
                print(f"{product.name}, Quantity: {quantity}, Price: ${item_price}")

            print("Total Amount:", total)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.order_history = []

    def login(self, entered_password):
        return self.password == entered_password

    def view_order_history(self):
        for order in self.order_history:
            order.check_cart()

if __name__ == "__main__":
    Biscuits= Product(1, "Biscuits", 100, 10)
    Chair= Product(2,"Chair", 1500, 20)
    Spoon = Product(3, "Spoon", 150, 35)
    user1 = User("john_doe", "password123")
    if user1.login("password123"):
        cart = Shopping()
        cart.add_prod(Biscuits, 2)
        cart.add_prod(Chair, 1)
        cart.add_prod(Spoon, 3)
        cart.check_cart()
        cart.remove_product(Biscuits, 1)
        user1.order_history.append(cart)
        user1.view_order_history()
    else:
        print("Login failed. Incorrect password.")


