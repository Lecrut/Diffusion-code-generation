from typing import List

PRODUCTS = {
    "Electronics": [
        {"name": "Laptop", "price": 999},
        {"name": "Smartphone", "price": 499},
        {"name": "Tablet", "price": 299}
    ],
    "Accessories": [
        {"name": "Headphones", "price": 199},
        {"name": "Camera", "price": 399}
    ]
}

def get_product_items(category: str = None) -> List[str]:
    if category:
        return [product["name"] for product in PRODUCTS.get(category, [])]
    else:
        all_products = []
        for products in PRODUCTS.values():
            all_products.extend([product["name"] for product in products])
        return all_products

if __name__ == '__main__':
    print("All Products:")
    print(get_product_items())
    print("\nElectronics:")
    print(get_product_items("Electronics"))
    print("\nAccessories:")
    print(get_product_items("Accessories"))