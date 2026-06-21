class FruitColorMap:
    def __init__(self):
        self.fruit_colors = {}

    def add_pair(self, fruit, color):
        self.fruit_colors[fruit] = color

    def get_color(self, fruit):
        return self.fruit_colors.get(fruit)

if __name__ == '__main__':
    manager = FruitColorMap()
    manager.add_pair("Apple", "Red")
    manager.add_pair("Banana", "Yellow")
    manager.add_pair("Grape", "Purple")
    print("--- Stored Fruit and Color Pairs ---")
    print(f"Apple: {manager.get_color('Apple')}")
    print(f"Banana: {manager.get_color('Banana')}")
    print(f"Grape: {manager.get_color('Grape')}")