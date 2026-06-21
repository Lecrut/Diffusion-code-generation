class FruitColorMapper:
    FRUIT_COLORS = {
        'apple': 'red',
        'banana': 'yellow',
        'grape': 'purple',
        'orange': 'orange',
        'strawberry': 'red'
    }

    @staticmethod
    def print_fruit_colors(color_map):
        for fruit, color in color_map.items():
            print(f'{fruit.capitalize()} is {color}.')

if __name__ == '__main__':
    mapper = FruitColorMapper()
    mapper.print_fruit_colors(FruitColorMapper.FRUIT_COLORS)