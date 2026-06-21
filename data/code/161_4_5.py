from typing import List

class ProductCatalog:
    def __init__(self):
        self.items = [
            "Laptop",
            "Smartphone",
            "Tablet",
            "Headphones",
            "Camera"
        ]

    def get_items(self) -> List[str]:
        return self.items

if __name__ == '__main__':
    catalog = ProductCatalog()
    products = catalog.get_items()
    print(products)