class FruitColorMapper:
    FRUIT_COLORS = {
        'apple': 'red',
        'banana': 'yellow',
        'grape': 'purple',
        'orange': 'orange',
        'strawberry': 'red',
        'lemon': 'yellow'
    }

    @staticmethod
    def pair_fruits_with_colors(fruit_list):
        return [(fruit, FruitColorMapper.FRUIT_COLORS.get(fruit, 'unknown')) for fruit in fruit_list]

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'grape', 'orange', 'strawberry', 'lemon']
    mapper = FruitColorMapper()
    print(mapper.pair_fruits_with_colors(fruits))