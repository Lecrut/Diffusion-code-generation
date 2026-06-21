class FruitColorMap:

    def __init__(self):
        self._map = {}

    def add(self, fruit, color):
        self._map[fruit] = color

    def get_color(self, fruit):
        return self._map.get(fruit, None)
if __name__ == '__main__':
    fc_map = FruitColorMap()
    fc_map.add('apple', 'red')
    fc_map.add('banana', 'yellow')
    print(fc_map.get_color('apple'))
    print(fc_map.get_color('grape'))