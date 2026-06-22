class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, weight_grams):
        self.items.append((item_name, weight_grams))

    def calculate_total_weight_kg(self):
        total_weight_grams = sum(weight for _, weight in self.items)
        return total_weight_grams / 1000

if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add_item("apple", 200)
    cart.add_item("banana", 150)
    cart.add_item("orange", 300)
    print(cart.calculate_total_weight_kg())