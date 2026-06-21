product_ids = {
    "Laptop": 101,
    "Smartphone": 202,
    "Tablet": 303,
    "Monitor": 404,
    "Keyboard": 505
}

def map_product_names_to_ids(product_list):
    return {product: product_ids.get(product, None) for product in product_list}

if __name__ == '__main__':
    sample_products = ["Laptop", "Smartphone", "Headphones"]
    mapped_ids = map_product_names_to_ids(sample_products)
    print(mapped_ids)