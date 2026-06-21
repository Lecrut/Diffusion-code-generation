from typing import List

class ProductManager:
    def __init__(self):
        self.products: List[str] = [
            "Laptop",
            "Smartphone",
            "Tablet",
            "Headphones",
            "Camera"
        ]

    def get_all_products(self) -> List[str]:
        return self.products

    def get_first_n_products(self, n: int) -> List[str]:
        return self.products[:n]

if __name__ == '__main__':
    manager = ProductManager()
    all_products = manager.get_all_products()
    first_three = manager.get_first_n_products(3)
    print("All Products:", all_products)
    print("First Three Products:", first_three)