import operator

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def find_max_product(products, attr='price'):
    if not products:
        raise ValueError("Input list cannot be empty")
    
    max_product = max(products, key=operator.attrgetter(attr))
    return max_product

if __name__ == '__main__':
    products = [
        Product('Laptop', 1200),
        Product('Smartphone', 800),
        Product('Tablet', 400)
    ]
    
    max_price_product = find_max_product(products, 'price')
    print(f"Max price product: {max_price_product.name} with price ${max_price_product.price}")
    
    max_name_length_product = find_max_product(products, 'name')
    print(f"Max name length product: {max_name_length_product.name} with length {len(max_name_length_product.name)}")