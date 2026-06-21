fruit_colors = {
    'apple': 'red',
    'banana': 'yellow',
    'grape': 'purple',
    'orange': 'orange',
    'strawberry': 'red'
}

class FruitColorMapper:
    def __init__(self, color_map):
        self.color_map = color_map

    def print_fruit_colors(self):
        for fruit, color in self.color_map.items():
            print(f'{fruit.capitalize()} is {color}.')

if __name__ == '__main__':
    mapper = FruitColorMapper(fruit_colors)
    mapper.print_fruit_colors()