def filter_expensive_products(products):
    def is_expensive(product_price):
        return product_price > 10

    expensive_products = {product: price for product, price in products.items() if is_expensive(price)}
    return expensive_products

if __name__ == '__main__':
    sample_products = {
        "Laptop": 1200,
        "Mouse": 25,
        "Keyboard": 75,
        "Monitor": 300,
        "USB Cable": 15
    }
    expensive_products = filter_expensive_products(sample_products)
    print("Expensive products:")
    for product, price in expensive_products.items():
        print(f"{product}: ${price}")