import heapq

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

def conditional_sort(products, k):
    if k >= len(products):
        return sorted(products)
    else:
        return heapq.nsmallest(k, products)

if __name__ == '__main__':
    products = [Product('apple', 1.2), Product('banana', 0.8), Product('cherry', 3.5)]
    top_k_products = conditional_sort(products, 2)
    for product in top_k_products:
        print(f'{product.name}: ${product.price}')