class FruitColorStore:

    def __init__(self):
        self.store = {}

    def add(self, fruit, color):
        self.store[fruit] = color

    def get_color(self, fruit):
        return self.store.get(fruit, None)
if __name__ == '__main__':
    store = FruitColorStore()
    store.add('orange', 'orange')
    store.add('grape', 'purple')
    print(store.get_color('orange'))
    print(store.get_color('grape'))
    print(store.get_color('apple'))