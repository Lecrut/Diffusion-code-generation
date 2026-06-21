from operator import attrgetter

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def find_max_product_by_price(products):
    if not products:
        raise ValueError("Input list cannot be empty")
    max_product = max(products, key=attrgetter('price'))
    return max_product

if __name__ == '__main__':
    products = [
        Product("Laptop", 1200),
        Product("Smartphone", 800),
        Product("Tablet", 450)
    ]
    max_price_product = find_max_product_by_price(products)
    print(f"Max price product: {max_price_product.name} with price {max_price_product.price}")