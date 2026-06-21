class FruitColorStore:
    FRUITS = ('orange', 'grape')
    COLORS = ('orange', 'purple')

    def __init__(self):
        self.store = {fruit: color for fruit, color in zip(self.FRUITS, self.COLORS)}

    def get_color(self, fruit):
        return self.store.get(fruit, None)

if __name__ == '__main__':
    fcs = FruitColorStore()
    print(fcs.get_color('orange'))
    print(fcs.get_color('grape'))