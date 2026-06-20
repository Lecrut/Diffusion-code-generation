import heapq

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def conditional_sort(products, k, min_price):
    filtered_products = [product for product in products if product.price >= min_price]
    return heapq.nsmallest(k, filtered_products, key=lambda x: x.price)

if __name__ == '__main__':
    products = [
        Product('Laptop', 1200),
        Product('Mouse', 30),
        Product('Keyboard', 50),
        Product('Monitor', 80)
    ]
    
    k = 3
    min_price = 40
    
    result = conditional_sort(products, k, min_price)
    for product in result:
        print(f'{product.name}: ${product.price}')