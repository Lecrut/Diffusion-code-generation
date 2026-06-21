from collections import defaultdict
from typing import List, NamedTuple

class Product(NamedTuple):
    id: int
    category: str
    price: float

GROUPING_FIELD = 'category'

def group_products_by_category(products: List[Product]) -> dict:
    groups = defaultdict(list)
    for product in products:
        groups[product.category].append(product)
    return dict(groups)

if __name__ == '__main__':
    sample_products = [
        Product(1, 'Electronics', 99.99),
        Product(2, 'Clothing', 19.99),
        Product(3, 'Electronics', 59.99),
        Product(4, 'Books', 14.99)
    ]
    
    grouped_products = group_products_by_category(sample_products)
    print(grouped_products)