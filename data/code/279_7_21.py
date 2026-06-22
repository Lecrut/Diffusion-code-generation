def filter_expensive_products(products):
    expensive_products = {product: price for product, price in products.items() if price > 10}
    return expensive_products
if __name__ == '__main__':
    sample_products = {'Laptop': 999.99, 'Mouse': 25.99, 'Keyboard': 49.99, 'Monitor': 129.99}
    expensive = filter_expensive_products(sample_products)
    print(expensive)