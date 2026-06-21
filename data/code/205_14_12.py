class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"

class InventoryManager:
    @staticmethod
    def sort_products_by_price(products):
        return sorted(products, key=lambda product: product.price)

if __name__ == '__main__':
    products = [
        Product("Laptop", 1200),
        Product("Smartphone", 800),
        Product("Tablet", 600)
    ]
    sorted_products = InventoryManager.sort_products_by_price(products)
    print(sorted_products)