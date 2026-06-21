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

if __name__ == '__main__':
    sample_pairs = FRUIT_COLOR_DATA[:3]
    print("Sample fruit and color pairs:")
    for pair in sample_pairs:
        print(f"Fruit: {pair.fruit}, Color: {pair.color}")