class FruitColorMap:

    def __init__(self):
        self.map = {}

    def add_fruit_color(self, fruit, color):
        self.map[fruit] = color

    def get_color(self, fruit):
        return self.map.get(fruit, None)
if __name__ == '__main__':
    fc_map = FruitColorMap()
    fc_map.add_fruit_color('orange', 'orange')
    fc_map.add_fruit_color('grape', 'purple')
    print(fc_map.get_color('orange'))
    print(fc_map.get_color('grape'))
    print(fc_map.get_color('apple'))