from typing import List

class ProductCatalog:
    def __init__(self):
        self.products = [
            "Laptop",
            "Smartphone",
            "Tablet",
            "Headphones",
            "Camera"
        ]

    def get_all_products(self) -> List[str]:
        return self.products

if __name__ == '__main__':
    catalog = ProductCatalog()
    all_products = catalog.get_all_products()
    print(all_products)