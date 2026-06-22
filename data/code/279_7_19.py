def filter_expensive_products(products):
    for product, price in products.items():
        if price > 10:
            print(f"{product}: ${price}")

if __name__ == '__main__':
    sample_products = {
        "Laptop": 999.99,
        "Mouse": 25.00,
        "Keyboard": 45.00,
        "Monitor": 150.00
    }
    filter_expensive_products(sample_products)