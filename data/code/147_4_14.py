class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def sort_products_by_price(products):
    return sorted(products, key=lambda p: p.price)

if __name__ == '__main__':
    products = [Product('apple', 1.0), Product('banana', 0.5), Product('cherry', 2.0)]
    sorted_products = sort_products_by_price(products)
    for product in sorted_products:
        print(f"{product.name}: ${product.price}")