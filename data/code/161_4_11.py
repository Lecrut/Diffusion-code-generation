from typing import List

class ProductCatalog:
    PRODUCT_ITEMS: List[str] = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Camera']

    @staticmethod
    def get_product_items() -> List[str]:
        return ProductCatalog.PRODUCT_ITEMS
if __name__ == '__main__':
    products = ProductCatalog.get_product_items()
    print(products)