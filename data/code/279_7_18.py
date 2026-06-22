def filter_expensive_products(products):
    for product, price in products.items():
        if price > 10:
            print(product)

if __name__ == '__main__':
    sample_products = {
        "Apple": 5,
        "Banana": 3,
        "Cherry": 20,
        "Date": 8,
        "Elderberry": 6
    }
    filter_expensive_products(sample_products)