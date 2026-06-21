class FruitColorManager:
    def __init__(self):
        self.fruit_colors = {}

    def add_pair(self, fruit, color):
        if not isinstance(fruit, str) or not isinstance(color, str):
            raise ValueError("Both fruit and color must be strings.")
        self.fruit_colors[fruit] = color

    def get_color_by_fruit(self, fruit):
        if fruit not in self.fruit_colors:
            raise KeyError(f"Fruit '{fruit}' not found.")
        return self.fruit_colors[fruit]

if __name__ == '__main__':
    manager = FruitColorManager()
    manager.add_pair("Apple", "Red")
    manager.add_pair("Banana", "Yellow")
    manager.add_pair("Grape", "Purple")

    print("--- Stored Fruit and Color Pairs ---")
    try:
        print(f"Color of Apple: {manager.get_color_by_fruit('Apple')}")
        print(f"Color of Banana: {manager.get_color_by_fruit('Banana')}")
        print(f"Color of Grape: {manager.get_color_by_fruit('Grape')}")
        print(f"Color of Orange: {manager.get_color_by_fruit('Orange')}")
    except KeyError as e:
        print(e)