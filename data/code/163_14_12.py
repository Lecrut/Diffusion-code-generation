from collections import namedtuple

FruitColor = namedtuple('FruitColor', ['fruit', 'color'])

FRUIT_COLORS = (
    FruitColor(fruit='apple', color='red'),
    FruitColor(fruit='banana', color='yellow'),
    FruitColor(fruit='grape', color='purple'),
)

if __name__ == '__main__':
    for fruit_color in FRUIT_COLORS:
        print(f"Fruit: {fruit_color.fruit}, Color: {fruit_color.color}")