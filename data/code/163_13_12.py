class FruitColorMapper:

    def __init__(self):
        self.fruit_color_dict = {}

    def map_fruits_to_colors(self, fruits, colors):
        for fruit, color in zip(fruits, colors):
            if fruit in self.fruit_color_dict:
                print(f"Warning: Key collision detected for {fruit}. Overwriting value from '{self.fruit_color_dict[fruit]}' to '{color}'.")
            self.fruit_color_dict[fruit] = color

    def get_fruit_color(self, fruit):
        return self.fruit_color_dict.get(fruit, 'Fruit not found')
if __name__ == '__main__':
    mapper = FruitColorMapper()
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'green']
    mapper.map_fruits_to_colors(fruits, colors)
    print(mapper.get_fruit_color('apple'))
    print(mapper.get_fruit_color('banana'))
    print(mapper.get_fruit_color('cherry'))
    print(mapper.get_fruit_color('grape'))