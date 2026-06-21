class FruitColorGenerator:
    @staticmethod
    def create_fruit_color_dict(fruits, colors):
        return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'green']
    fruit_color_dict = FruitColorGenerator.create_fruit_color_dict(fruits, colors)
    print(fruit_color_dict)