from typing import List

def validate_data(data: List[str]) -> None:
    if not all(isinstance(item, str) for item in data):
        raise ValueError("All items must be strings.")
    if len(data) == 0:
        raise ValueError("Data list cannot be empty.")

def get_product_items() -> List[str]:
    product_list = [
        "Laptop",
        "Smartphone",
        "Tablet",
        "Headphones",
        "Camera"
    ]
    validate_data(product_list)
    return product_list

if __name__ == '__main__':
    products = get_product_items()
    print(products)