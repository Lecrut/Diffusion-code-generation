product_ids = {
    'Laptop': 101,
    'Smartphone': 202,
    'Tablet': 303,
    'Monitor': 404,
    'Keyboard': 505
}

def map_product_to_id(product_list):
    return {product: product_ids[product] for product in product_list if product in product_ids}

if __name__ == '__main__':
    sample_products = ['Laptop', 'Smartphone', 'Mouse']
    print(map_product_to_id(sample_products))