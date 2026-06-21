class FruitColorMap:
    def __init__(self):
        self.map = {'banana': 'yellow', 'grapefruit': 'pink'}

    def get_color(self, fruit):
        return self.map.get(fruit, None)

if __name__ == '__main__':
    fc = FruitColorMap()
    print(fc.get_color('banana'))
    print(fc.get_color('grapefruit'))