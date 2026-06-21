class FruitColorMap:

    def __init__(self):
        self._map = {}

    def add(self, fruit, color):
        self._map[fruit] = color

    def get_color(self, fruit):
        return self._map.get(fruit, None)
if __name__ == '__main__':
    fc = FruitColorMap()
    fc.add('apple', 'red')
    fc.add('banana', 'yellow')
    print(fc.get_color('apple'))
    print(fc.get_color('grape'))