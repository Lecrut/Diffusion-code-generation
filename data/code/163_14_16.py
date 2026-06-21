from collections import namedtuple

FruitColorPair = namedtuple('FruitColorPair', ['fruit', 'color'])

FRUIT_COLOR_DATA = (
    FruitColorPair(fruit='Apple', color='Red'),
    FruitColorPair(fruit='Banana', color='Yellow'),
    FruitColorPair(fruit='Cherry', color='Red'),
    FruitColorPair(fruit='Grape', color='Purple'),
)

if __name__ == '__main__':
    for pair in FRUIT_COLOR_DATA:
        print(pair)