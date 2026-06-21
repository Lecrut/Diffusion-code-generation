product_ids = {
    "Apple": 1,
    "Banana": 2,
    "Cherry": 3,
    "Date": 4,
    "Elderberry": 5
}

def map_product_to_id(product_names):
    return {product: product_ids.get(product, None) for product in product_names}

if __name__ == '__main__':
    sample_products = ["Apple", "Banana", "Grape"]
    print(map_product_to_id(sample_products))