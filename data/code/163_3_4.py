class FruitColorStore:

    def __init__(self):
        self.store = {}

    def add_fruit_color(self, fruit, color):
        self.store[fruit] = color

    def get_color(self, fruit):
        return self.store.get(fruit, None)
if __name__ == '__main__':
    store = FruitColorStore()
    store.add_fruit_color('orange', 'orange')
    store.add_fruit_color('grape', 'purple')
    print(store.get_color('orange'))
    print(store.get_color('grape'))
    print(store.get_color('apple'))