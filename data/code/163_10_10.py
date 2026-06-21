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
    sample_data = {
        'kiwi': 'green',
        'melon': 'yellow',
        'pear': 'green'
    }
    extended_color_map = FruitColorMapper.FRUIT_COLORS | sample_data
    FruitColorMapper.print_fruit_colors(extended_color_map)