class ProductFilter:
    def __init__(self, products):
        self.products = products

    def filter_expensive_products(self):
        for product, price in self.products.items():
            if price > 10:
                print(f"{product}: ${price}")

if __name__ == '__main__':
    sample_products = {
        "Laptop": 999,
        "Mouse": 25,
        "Keyboard": 45,
        "Monitor": 150
    }
    
    product_filter = ProductFilter(sample_products)
    product_filter.filter_expensive_products()