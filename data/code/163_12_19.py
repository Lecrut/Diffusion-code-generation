class FruitColorManager:

    def __init__(self):
        self.fruit_colors = {}

    def add_pair(self, fruit, color):
        if not isinstance(fruit, str) or not isinstance(color, str):
            raise ValueError('Both fruit and color must be strings.')
        self.fruit_colors[fruit] = color

    def get_color_by_fruit(self, fruit):
        if not isinstance(fruit, str):
            raise ValueError('Fruit must be a string.')
        return self.fruit_colors.get(fruit)
if __name__ == '__main__':
    manager = FruitColorManager()
    manager.add_pair('Apple', 'Red')
    manager.add_pair('Banana', 'Yellow')
    manager.add_pair('Grape', 'Purple')
    print('--- Stored Fruit and Color Pairs ---')
    for fruit, color in manager.fruit_colors.items():
        print(f'Fruit: {fruit}, Color: {color}')
    apple_color = manager.get_color_by_fruit('Apple')
    print(f'The color of an Apple is: {apple_color}')