class FruitColorMap:

    def __init__(self):
        self._map = {}

    def add(self, fruit, color):
        self._map[fruit] = color

    def get_color(self, fruit):
        return self._map.get(fruit, None)
if __name__ == '__main__':
    fcm = FruitColorMap()
    fcm.add('apple', 'red')
    fcm.add('banana', 'yellow')
    print(fcm.get_color('apple'))
    print(fcm.get_color('orange'))