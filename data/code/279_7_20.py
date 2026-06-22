class ProductFilter:
    def __init__(self, products):
        self.products = products

    def filter_expensive(self):
        for product, price in self.products.items():
            if price > 10:
                print(f"{product}: ${price}")

if __name__ == '__main__':
    sample_products = {
        "Laptop": 999,
        "Smartphone": 799,
        "Mouse": 25,
        "Keyboard": 49
    }
    
    filterer = ProductFilter(sample_products)
    filterer.filter_expensive()