class FruitColorStore:
    def __init__(self):
        self.store = {'orange': 'orange', 'grape': 'purple'}

    def get_color(self, fruit):
        return self.store.get(fruit, None)

if __name__ == '__main__':
    fc_store = FruitColorStore()
    print(fc_store.get_color('orange'))
    print(fc_store.get_color('grape'))