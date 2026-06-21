class FruitColorCache:
    def __init__(self):
        self.cache = {'orange': 'orange', 'grape': 'purple'}
    
    def get_color(self, fruit):
        return self.cache.get(fruit, None)

if __name__ == '__main__':
    fc = FruitColorCache()
    print(fc.get_color('orange'))
    print(fc.get_color('grape'))