product_ids = {
    'Laptop': 101,
    'Smartphone': 202,
    'Tablet': 303,
    'Monitor': 404,
    'Keyboard': 505
}

def map_product_names_to_ids(product_list):
    return {product: product_ids[product] for product in product_list if product in product_ids}

if __name__ == '__main__':
    sample_products = ['Laptop', 'Smartphone', 'Mouse']
    mapped_ids = map_product_names_to_ids(sample_products)
    print(mapped_ids)