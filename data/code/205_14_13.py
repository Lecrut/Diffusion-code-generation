class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def sort_products_by_price(products):
    return sorted(products, key=lambda product: product.price)

if __name__ == '__main__':
    products = [
        Product("Laptop", 1200),
        Product("Mouse", 25),
        Product("Keyboard", 75)
    ]
    sorted_products = sort_products_by_price(products)
    print(sorted_products)