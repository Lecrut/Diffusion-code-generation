class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def sort_products(products, attribute):
    return sorted(products, key=lambda product: getattr(product, attribute))

if __name__ == '__main__':
    products = [
        Product("Laptop", 1200),
        Product("Mouse", 30),
        Product("Keyboard", 50)
    ]
    sorted_by_price = sort_products(products, 'price')
    print([(product.name, product.price) for product in sorted_by_price])