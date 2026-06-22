def filter_expensive_products(products):
    def is_expensive(price):
        return price > 10

    for product, price in products.items():
        if is_expensive(price):
            print(product)

if __name__ == '__main__':
    sample_products = {
        'Laptop': 1200,
        'Smartphone': 800,
        'Tablet': 300,
        'Monitor': 250,
        'Keyboard': 60
    }
    filter_expensive_products(sample_products)