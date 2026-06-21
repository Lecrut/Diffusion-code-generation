class FruitColorManager:

    def __init__(self):
        self.fruit_colors = {}

    def add_pair(self, fruit, color):
        if not isinstance(fruit, str) or not isinstance(color, str):
            raise ValueError('Both fruit and color must be strings.')
        self.fruit_colors[fruit] = color

    def get_color(self, fruit):
        if not isinstance(fruit, str):
            raise ValueError('Fruit name must be a string.')
        return self.fruit_colors.get(fruit, None)
if __name__ == '__main__':
    manager = FruitColorManager()
    manager.add_pair('Apple', 'Red')
    manager.add_pair('Banana', 'Yellow')
    manager.add_pair('Grape', 'Purple')
    print('--- Stored Fruit and Color Pairs ---')
    print(f'Apple color: {manager.get_color('Apple')}')
    print(f'Banana color: {manager.get_color('Banana')}')
    print(f'Grape color: {manager.get_color('Grape')}')
    print(f'Orange color: {manager.get_color('Orange')}')