from typing import List

def get_product_items() -> List[str]:
    return [
        "Laptop",
        "Smartphone",
        "Tablet",
        "Headphones",
        "Camera"
    ]

if __name__ == '__main__':
    products = get_product_items()
    print(products)