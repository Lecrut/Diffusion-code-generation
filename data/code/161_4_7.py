from typing import List

def get_product_items() -> List[str]:
    products = {'Electronics': ['Laptop', 'Smartphone', 'Tablet'], 'Accessories': ['Headphones', 'Camera']}
    return [item for category in products.values() for item in category]
if __name__ == '__main__':
    products = get_product_items()
    print(products)