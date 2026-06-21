class FruitColorMapper:

    def __init__(self):
        self.fruit_color_dict = {}

    def map_fruits_to_colors(self, fruits, colors):
        self.fruit_color_dict = {fruit: color for fruit, color in zip(fruits, colors)}

    def get_fruit_color(self, fruit):
        return self.fruit_color_dict.get(fruit, 'Unknown')
if __name__ == '__main__':
    mapper = FruitColorMapper()
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'red']
    mapper.map_fruits_to_colors(fruits, colors)
    print(mapper.get_fruit_color('apple'))
    print(mapper.get_fruit_color('banana'))
    print(mapper.get_fruit_color('cherry'))
    print(mapper.get_fruit_color('grape'))