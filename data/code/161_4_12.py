from typing import List

PRODUCT_ITEMS: List[str] = [
    "Laptop",
    "Smartphone",
    "Tablet",
    "Headphones",
    "Camera"
]

def get_product_items() -> List[str]:
    return PRODUCT_ITEMS

if __name__ == '__main__':
    products = get_product_items()
    print(products)