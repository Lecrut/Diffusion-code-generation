from typing import List

def get_product_items() -> List[str]:
    return [
        "T-shirt",
        "Jeans",
        "Sneakers",
        "Hat",
        "Gloves"
    ]

if __name__ == '__main__':
    products = get_product_items()
    print(products)