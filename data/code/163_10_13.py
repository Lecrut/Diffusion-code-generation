class FruitColorMapper:
    def __init__(self):
        self.fruit_colors = {
            'apple': 'red',
            'banana': 'yellow',
            'grape': 'purple',
            'orange': 'orange',
            'strawberry': 'red'
        }

    def print_fruit_colors(self):
        for fruit, color in self.fruit_colors.items():
            print(f'{fruit.capitalize()} is {color}.')

if __name__ == '__main__':
    mapper = FruitColorMapper()
    mapper.print_fruit_colors()