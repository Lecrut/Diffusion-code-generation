def filter_expensive_products(products):
    for product, price in products.items():
        if price > 10:
            print(product)

if __name__ == '__main__':
    sample_products = {
        "Laptop": 999,
        "Mouse": 25,
        "Keyboard": 45,
        "Monitor": 80
    }
    filter_expensive_products(sample_products)