class FruitColorMap:

    def __init__(self):
        self._map = {}

    def add_pair(self, fruit, color):
        self._map[fruit] = color

    def get_color(self, fruit):
        return self._map.get(fruit, None)
if __name__ == '__main__':
    fc = FruitColorMap()
    fc.add_pair('apple', 'red')
    fc.add_pair('banana', 'yellow')
    print(fc.get_color('apple'))
    print(fc.get_color('grape'))