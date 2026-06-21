class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}: ${self.price}"

def sort_products_by_price(products):
    if not all(isinstance(product, Product) for product in products):
        raise ValueError("All elements must be instances of Product")
    return sorted(products, key=lambda product: product.price)

if __name__ == '__main__':
    products = [
        Product("Laptop", 1200),
        Product("Mouse", 35),
        Product("Keyboard", 60)
    ]
    sorted_products = sort_products_by_price(products)
    print(sorted_products)