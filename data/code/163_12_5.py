class FruitColorMap:

    def __init__(self):
        self.map = {}

    def add_pair(self, fruit, color):
        self.map[fruit] = color

    def get_color(self, fruit):
        return self.map.get(fruit, None)
if __name__ == '__main__':
    fc_map = FruitColorMap()
    fc_map.add_pair('apple', 'red')
    fc_map.add_pair('banana', 'yellow')
    print(fc_map.get_color('apple'))
    print(fc_map.get_color('grape'))