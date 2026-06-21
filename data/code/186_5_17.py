class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f"{self.name}: ${self.price}"

def validate_products(products):
    if not all(isinstance(p, Product) for p in products):
        raise ValueError("All items must be instances of the Product class")

def sort_products_by_price(products):
    validate_products(products)
    return sorted(products, key=lambda product: product.price)

if __name__ == '__main__':
    products = [
        Product("Laptop", 1200),
        Product("Mouse", 50),
        Product("Keyboard", 100),
        Product("Monitor", 300)
    ]
    sorted_products = sort_products_by_price(products)
    print(sorted_products)