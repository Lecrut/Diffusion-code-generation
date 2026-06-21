from typing import List

def fetch_product_list() -> List[str]:
    return [
        "Laptop",
        "Smartphone",
        "Tablet",
        "Headphones",
        "Camera"
    ]

if __name__ == '__main__':
    product_items = fetch_product_list()
    print(product_items)