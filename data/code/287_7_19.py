class ShoppingCart:
    def __init__(self):
        self.items = []

    @staticmethod
    def add_item(cart, item_name, weight_grams):
        cart.items.append((item_name, weight_grams))

    @classmethod
    def calculate_total_weight(cls, cart):
        total_weight_grams = sum(item[1] for item in cart.items)
        return total_weight_grams / 1000

if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    ShoppingCart.add_item(shopping_cart, "apple", 200)
    ShoppingCart.add_item(shopping_cart, "banana", 150)
    ShoppingCart.add_item(shopping_cart, "orange", 300)
    
    total_weight_kg = ShoppingCart.calculate_total_weight(shopping_cart)
    print(total_weight_kg)