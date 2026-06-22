class ProductFilter:
    def __init__(self, products):
        self.products = products

    def filter_expensive(self, price_threshold=10):
        return {product: price for product, price in self.products.items() if price > price_threshold}

if __name__ == '__main__':
    sample_products = {
        "Laptop": 999,
        "Mouse": 25,
        "Keyboard": 45,
        "Monitor": 150,
        "USB Cable": 7
    }
    filter_instance = ProductFilter(sample_products)
    expensive_products = filter_instance.filter_expensive()
    for product, price in expensive_products.items():
        print(f"{product}: ${price}")