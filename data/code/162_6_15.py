class PriceCache:
    def __init__(self, initial_data=None):
        self.cache = initial_data if initial_data else {}

    @staticmethod
    def from_dict(data):
        return PriceCache(data)

    def get_price(self, product_name, default=None):
        return self.cache.get(product_name, default)

if __name__ == '__main__':
    sample_prices = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4
    }
    price_cache = PriceCache.from_dict(sample_prices)
    print(price_cache.get_price("apple"))
    print(price_cache.get_price("grape", default=5))