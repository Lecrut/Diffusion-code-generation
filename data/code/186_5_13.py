class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}: ${self.price}"

def sort_products_by_price(products):
    return sorted(products, key=lambda product: product.price)

if __name__ == '__main__':
    products = [Product("Laptop", 1200), Product("Mouse", 30), Product("Keyboard", 50)]
    sorted_products = sort_products_by_price(products)
    print(sorted_products)