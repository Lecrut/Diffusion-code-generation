from collections import namedtuple

FruitColor = namedtuple('FruitColor', ['fruit', 'color'])

FRUIT_COLOR_PAIRS = (
    FruitColor(fruit='Apple', color='Red'),
    FruitColor(fruit='Banana', color='Yellow'),
    FruitColor(fruit='Cherry', color='Red'),
)

if __name__ == '__main__':
    for pair in FRUIT_COLOR_PAIRS:
        print(pair)