from typing import List

def validate_input(data: List[str]) -> None:
    if not data or not all(isinstance(item, str) for item in data):
        raise ValueError("Input must be a non-empty list of strings.")

def get_product_items() -> List[str]:
    product_list = [
        "Laptop",
        "Smartphone",
        "Tablet",
        "Headphones",
        "Camera"
    ]
    validate_input(product_list)
    return product_list

if __name__ == '__main__':
    products = get_product_items()
    print(products)