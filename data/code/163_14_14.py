from collections import namedtuple

FruitColorPair = namedtuple('FruitColorPair', ['fruit', 'color'])

FRUIT_COLOR_DATA = (
    FruitColorPair('apple', 'red'),
    FruitColorPair('banana', 'yellow'),
    FruitColorPair('grape', 'purple'),
    FruitColorPair('orange', 'orange'),
    FruitColorPair('strawberry', 'red'),
    FruitColorPair('kiwi', 'brown')
)

class FruitColorManager:
    def __init__(self, data):
        self.data = data

    def get_fruit_colors(self):
        return self.data

if __name__ == '__main__':
    manager = FruitColorManager(FRUIT_COLOR_DATA)
    fruit_colors = manager.get_fruit_colors()
    for pair in fruit_colors:
        print(f"Fruit: {pair.fruit}, Color: {pair.color}")