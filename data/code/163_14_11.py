from collections import namedtuple

FruitColor = namedtuple('FruitColor', ['fruit', 'color'])

FRUIT_COLOR_PAIRS = (
    FruitColor(fruit='Apple', color='Red'),
    FruitColor(fruit='Banana', color='Yellow'),
    FruitColor(fruit='Cherry', color='Red'),
    FruitColor(fruit='Grape', color='Purple'),
)

if __name__ == '__main__':
    for fruit_color in FRUIT_COLOR_PAIRS:
        print(f'{fruit_color.fruit}: {fruit_color.color}')