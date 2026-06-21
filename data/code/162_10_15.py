product_ids = {
    "Apple": 101,
    "Banana": 102,
    "Cherry": 103,
    "Date": 104,
    "Elderberry": 105
}

def map_product_to_id(products):
    return {product: product_ids[product] for product in products if product in product_ids}

if __name__ == '__main__':
    sample_products = ["Apple", "Banana", "Grape"]
    print(map_product_to_id(sample_products))