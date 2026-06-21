class FruitColorMap:
    def __init__(self):
        self.fruit_colors = {}

    def add_pair(self, fruit, color):
        self.fruit_colors[fruit] = color

    def get_color(self, fruit):
        return self.fruit_colors.get(fruit, "Unknown")

if __name__ == '__main__':
    manager = FruitColorMap()
    manager.add_pair("Apple", "Red")
    manager.add_pair("Banana", "Yellow")
    manager.add_pair("Grape", "Purple")
    manager.add_pair("Orange", "Orange")
    print("--- Stored Fruit and Color Pairs ---")
    apple_color = manager.get_color("Apple")
    banana_color = manager.get_color("Banana")
    grape_color = manager.get_color("Grape")
    orange_color = manager.get_color("Orange")
    unknown_color = manager.get_color("Watermelon")

    print(f"Apple: {apple_color}")
    print(f"Banana: {banana_color}")
    print(f"Grape: {grape_color}")
    print(f"Orange: {orange_color}")
    print(f"Watermelon: {unknown_color}")