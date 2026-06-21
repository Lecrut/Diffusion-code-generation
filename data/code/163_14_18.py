from collections import namedtuple

FruitColor = namedtuple('FruitColor', ['fruit', 'color'])

FRUIT_COLOR_PAIRS = (
    FruitColor(fruit='apple', color='red'),
    FruitColor(fruit='banana', color='yellow'),
    FruitColor(fruit='grape', color='purple'),
    FruitColor(fruit='orange', color='orange'),
)

if __name__ == '__main__':
    for pair in FRUIT_COLOR_PAIRS:
        print(pair)