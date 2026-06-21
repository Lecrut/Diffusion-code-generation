product_ids = {
    'Laptop': 101,
    'Smartphone': 202,
    'Tablet': 303,
    'Headphones': 404,
    'Mouse': 505
}

def map_product_to_id(product_names):
    return {product: product_ids.get(product, None) for product in product_names}

if __name__ == '__main__':
    sample_products = ['Laptop', 'Smartphone', 'Monitor']
    print(map_product_to_id(sample_products))