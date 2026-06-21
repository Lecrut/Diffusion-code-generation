class FruitColorMapper:
    @staticmethod
    def create_fruit_color_dict(fruits, colors):
        return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'red']
    fruit_color_dict = FruitColorMapper.create_fruit_color_dict(fruits, colors)
    print(fruit_color_dict)