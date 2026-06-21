from typing import List

def validate_product_items(items: List[str]) -> None:
    if not all(isinstance(item, str) for item in items):
        raise ValueError("All product items must be strings")
    if len(items) != 5:
        raise ValueError("Product items list must contain exactly 5 elements")

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
    validate_product_items(products)
    print(products)