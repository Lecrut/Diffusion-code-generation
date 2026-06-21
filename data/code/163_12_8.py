class FruitColorManager:

    def __init__(self):
        self.fruit_colors = {}

    def add_pair(self, fruit, color):
        self.fruit_colors[fruit] = color

    def get_color(self, fruit):
        return self.fruit_colors.get(fruit, None)
if __name__ == '__main__':
    manager = FruitColorManager()
    manager.add_pair('Apple', 'Red')
    manager.add_pair('Banana', 'Yellow')
    manager.add_pair('Grape', 'Purple')
    print('--- Stored Fruit and Color Pairs ---')
    colors = {'Apple': manager.get_color('Apple'), 'Banana': manager.get_color('Banana'), 'Grape': manager.get_color('Grape'), 'Orange': manager.get_color('Orange')}
    for fruit, color in colors.items():
        print(f'Fruit: {fruit}, Color: {color}')