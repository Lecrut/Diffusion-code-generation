class FruitColorMap:

    def __init__(self):
        self.map = {'orange': 'orange', 'grape': 'purple'}

    def get_color(self, fruit):
        if fruit not in self.map:
            raise ValueError(f'Invalid fruit: {fruit}')
        return self.map[fruit]
if __name__ == '__main__':
    fc = FruitColorMap()
    try:
        print(fc.get_color('orange'))
        print(fc.get_color('grape'))
        print(fc.get_color('apple'))
    except ValueError as e:
        print(e)