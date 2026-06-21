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

class FruitColorPairs:
    data = FRUIT_COLOR_DATA

    @staticmethod
    def get_pairs():
        return FruitColorPairs.data

if __name__ == '__main__':
    pairs = FruitColorPairs.get_pairs()
    for pair in pairs:
        print(f"Fruit: {pair.fruit}, Color: {pair.color}")