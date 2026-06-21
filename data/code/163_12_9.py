class FruitColorManager:
    def __init__(self):
        self.fruit_colors = {}

    def add_pair(self, fruit, color):
        self.fruit_colors[fruit] = color

    def get_color_by_fruit(self, fruit):
        return self.fruit_colors.get(fruit, "Unknown")

if __name__ == '__main__':
    manager = FruitColorManager()
    manager.add_pair("Apple", "Red")
    manager.add_pair("Banana", "Yellow")
    manager.add_pair("Grape", "Purple")
    print("--- Color by Fruit ---")
    print(manager.get_color_by_fruit("Apple"))
    print(manager.get_color_by_fruit("Banana"))
    print(manager.get_color_by_fruit("Grape"))
    print(manager.get_color_by_fruit("Orange"))