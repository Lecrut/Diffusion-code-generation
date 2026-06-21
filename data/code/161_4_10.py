from typing import List

PRODUCT_ITEMS = {
    "Electronics": ["Laptop", "Smartphone", "Tablet"],
    "Audio": ["Headphones", "Speakers"],
    "Photography": ["Camera"]
}

def get_product_items(category: str) -> List[str]:
    return PRODUCT_ITEMS.get(category, [])

if __name__ == '__main__':
    electronics = get_product_items("Electronics")
    print(electronics)