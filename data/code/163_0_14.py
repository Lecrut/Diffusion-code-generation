class FruitColors:

    def __init__(self):
        self.color_map = {'apple': 'red', 'banana': 'yellow'}

    def get_color(self, fruit):
        return self.color_map.get(fruit, 'Unknown color')
if __name__ == '__main__':
    fruit_colors_instance = FruitColors()
    print(fruit_colors_instance.get_color('apple'))
    print(fruit_colors_instance.get_color('banana'))
    print(fruit_colors_instance.get_color('cherry'))