class FruitColorManager:
    def __init__(self):
        self.fruit_colors = []
    def add_pair(self, fruit, color):
        self.fruit_colors.append((fruit, color))
    def get_pairs(self):
        return self.fruit_colors
    def display_all(self):
        for fruit, color in self.fruit_colors:
            print(f"Fruit: {fruit}, Color: {color}")
if __name__ == '__main__':
    manager = FruitColorManager()
    manager.add_pair("Apple", "Red")
    manager.add_pair("Banana", "Yellow")
    manager.add_pair("Grape", "Purple")
    print("--- Stored Fruit and Color Pairs ---")
    pairs = manager.get_pairs()
    for fruit, color in pairs:
        print(f"Fruit: {fruit}, Color: {color}")