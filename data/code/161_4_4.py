from typing import List

PRODUCT_ITEMS: List[str] = [
    "Apple",
    "Banana",
    "Cherry",
    "Date",
    "Elderberry"
]

def get_product_items() -> List[str]:
    return PRODUCT_ITEMS

if __name__ == '__main__':
    print(get_product_items())