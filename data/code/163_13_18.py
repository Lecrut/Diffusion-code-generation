class FruitColorMapper:
    def __init__(self, fruits, colors):
        self.fruit_color_dict = {fruit: color for fruit, color in zip(fruits, colors)}

    def get_fruit_color(self, fruit):
        return self.fruit_color_dict.get(fruit, "Unknown")

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'green']
    mapper = FruitColorMapper(fruits, colors)
    print(mapper.get_fruit_color('apple'))
    print(mapper.get_fruit_color('banana'))
    print(mapper.get_fruit_color('cherry'))
    print(mapper.get_fruit_color('grape'))