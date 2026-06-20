import heapq

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def conditional_sort(products, k, min_price):
    filtered_products = [p for p in products if p.price >= min_price]
    top_k = heapq.nsmallest(k, filtered_products, key=lambda x: x.price)
    return top_k

if __name__ == '__main__':
    products = [
        Product("Laptop", 1200),
        Product("Smartphone", 800),
        Product("Tablet", 350),
        Product("Monitor", 250),
        Product("Keyboard", 100)
    ]
    k = 2
    min_price = 400
    result = conditional_sort(products, k, min_price)
    print([(p.name, p.price) for p in result])