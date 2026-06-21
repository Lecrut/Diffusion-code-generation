product_ids = {
    'Laptop': 101,
    'Smartphone': 202,
    'Tablet': 303,
    'Monitor': 404,
    'Keyboard': 505
}

def map_product_to_id(products):
    return {product: product_ids.get(product, None) for product in products}

if __name__ == '__main__':
    sample_products = ['Laptop', 'Smartphone', 'Mouse']
    mapped_ids = map_product_to_id(sample_products)
    print(mapped_ids)