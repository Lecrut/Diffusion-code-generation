class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, weight_grams):
        self.items.append((item_name, weight_grams))

    @staticmethod
    def calculate_total_weight(cart_items):
        total_weight_grams = sum(item[1] for item in cart_items)
        return total_weight_grams / 1000

if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    shopping_cart.add_item("apple", 200)
    shopping_cart.add_item("banana", 150)
    shopping_cart.add_item("orange", 300)
    
    print(ShoppingCart.calculate_total_weight(shopping_cart.items))