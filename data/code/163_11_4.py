class FruitColorMapper:
    def __init__(self):
        self.fruit_colors = {
            'apple': 'red',
            'banana': 'yellow',
            'grape': 'purple',
            'orange': 'orange',
            'strawberry': 'red',
            'lemon': 'yellow'
        }

    def pair_fruits_with_colors(self, fruit_list):
        return [(fruit, self.fruit_colors.get(fruit, 'unknown')) for fruit in fruit_list]

if __name__ == '__main__':
    mapper = FruitColorMapper()
    fruits = ['apple', 'banana', 'grape', 'orange', 'strawberry', 'lemon']
    print(mapper.pair_fruits_with_colors(fruits))