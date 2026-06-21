from collections import defaultdict
from typing import List, NamedTuple

class Product(NamedTuple):
    id: int
    category: str
    price: float

def group_products_by_category(products: List[Product]) -> dict:
    if not all(isinstance(p, Product) for p in products):
        raise ValueError("All items must be instances of Product")
    
    groups = defaultdict(list)
    for product in products:
        groups[product.category].append(product)
    
    return dict(groups)

if __name__ == '__main__':
    sample_products = [
        Product(1, 'Electronics', 99.99),
        Product(2, 'Clothing', 45.00),
        Product(3, 'Electronics', 199.99),
        Product(4, 'Books', 15.00)
    ]
    
    grouped_products = group_products_by_category(sample_products)
    print(grouped_products)