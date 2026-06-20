import heapq

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def conditional_sort(products, k):
    filtered_products = [product for product in products if product.price > 50]
    return heapq.nlargest(k, filtered_products, key=lambda x: x.price)

if __name__ == '__main__':
    products = [
        Product('Laptop', 800),
        Product('Smartphone', 300),
        Product('Tablet', 200),
        Product('Monitor', 150)
    ]
    k = 2
    result = conditional_sort(products, k)
    for product in result:
        print(f'{product.name}: ${product.price}')