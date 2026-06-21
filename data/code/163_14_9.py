from collections import namedtuple

FruitColorPair = namedtuple('FruitColorPair', ['fruit', 'color'])

FRUIT_COLOR_DATA = (
    FruitColorPair('apple', 'red'),
    FruitColorPair('banana', 'yellow'),
    FruitColorPair('grape', 'purple'),
)

if __name__ == '__main__':
    for pair in FRUIT_COLOR_DATA:
        print(f'{pair.fruit}: {pair.color}')