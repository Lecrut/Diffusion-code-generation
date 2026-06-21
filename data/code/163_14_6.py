from collections import namedtuple

FruitColor = namedtuple('FruitColor', ['fruit', 'color'])

FRUIT_COLOR_PAIRS = (
    FruitColor(fruit='apple', color='red'),
    FruitColor(fruit='banana', color='yellow'),
    FruitColor(fruit='grape', color='purple'),
)

if __name__ == '__main__':
    for fruit_color in FRUIT_COLOR_PAIRS:
        print(fruit_color)