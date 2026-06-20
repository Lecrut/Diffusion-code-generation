import heapq

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def conditional_sort(products, k):
    return heapq.nsmallest(k, products, key=lambda p: p.price)

if __name__ == '__main__':
    products = [
        Product("Laptop", 1200),
        Product("Smartphone", 800),
        Product("Tablet", 450),
        Product("Monitor", 300)
    ]
    top_k_products = conditional_sort(products, 2)
    for product in top_k_products:
        print(f"{product.name}: ${product.price}")