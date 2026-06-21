product_ids = {
    'Apple': 1,
    'Banana': 2,
    'Cherry': 3,
    'Date': 4,
    'Elderberry': 5
}

def map_product_names_to_ids(product_names):
    return {name: product_ids.get(name, None) for name in product_names}

if __name__ == '__main__':
    sample_products = ['Apple', 'Banana', 'Grape']
    print(map_product_names_to_ids(sample_products))