class ProductCache:

    def __init__(self):
        self.cache = {}

    def add_product(self, name, price):
        self.cache[name] = price

    def get_price(self, name):
        return self.cache.get(name, None)
if __name__ == '__main__':
    cache = ProductCache()
    cache.add_product('apple', 1)
    cache.add_product('banana', 2)
    cache.add_product('cherry', 3)
    print(cache.get_price('apple'))
    print(cache.get_price('grape'))