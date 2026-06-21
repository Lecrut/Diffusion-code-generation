class FruitColorManager:
    def __init__(self):
        self.fruit_colors = {}

    def add_pair(self, fruit, color):
        self.fruit_colors[fruit] = color

    def get_color(self, fruit):
        return self.fruit_colors.get(fruit)

if __name__ == '__main__':
    manager = FruitColorManager()
    manager.add_pair("Apple", "Red")
    manager.add_pair("Banana", "Yellow")
    manager.add_pair("Grape", "Purple")
    print("--- Stored Fruit and Color Pairs ---")
    for fruit, color in manager.fruit_colors.items():
        print(f"Fruit: {fruit}, Color: {color}")