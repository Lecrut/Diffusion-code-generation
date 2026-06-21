class FruitColorMap:

    def __init__(self):
        self.map = {'orange': 'orange', 'grape': 'purple'}

    def get_color(self, fruit):
        return self.map.get(fruit, None)
if __name__ == '__main__':
    fc = FruitColorMap()
    print(fc.get_color('orange'))
    print(fc.get_color('grape'))
    print(fc.get_color('apple'))