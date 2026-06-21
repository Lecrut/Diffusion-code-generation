class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Product(name={self.name}, price={self.price})'
DEFAULT_PRODUCTS = [Product('Laptop', 1200), Product('Mouse', 50), Product('Keyboard', 80), Product('Monitor', 300)]

def sort_products_by_price(products):
    return sorted(products, key=lambda product: product.price)
if __name__ == '__main__':
    products = DEFAULT_PRODUCTS
    sorted_products = sort_products_by_price(products)
    print(sorted_products)