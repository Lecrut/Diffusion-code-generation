from typing import List

PRODUCT_LIST = [
    "Laptop",
    "Smartphone",
    "Tablet",
    "Headphones",
    "Camera"
]

def get_product_items() -> List[str]:
    return PRODUCT_LIST

if __name__ == '__main__':
    products = get_product_items()
    print(products)