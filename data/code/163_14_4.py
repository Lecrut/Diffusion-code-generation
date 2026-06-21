from collections import namedtuple

FruitColorPair = namedtuple('FruitColorPair', ['fruit', 'color'])

FRUIT_COLOR_DATA = (
    FruitColorPair('Apple', 'Red'),
    FruitColorPair('Banana', 'Yellow'),
    FruitColorPair('Cherry', 'Red'),
    FruitColorPair('Grape', 'Purple'),
)

if __name__ == '__main__':
    for pair in FRUIT_COLOR_DATA:
        print(pair)