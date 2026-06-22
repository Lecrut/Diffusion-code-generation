products = {
    "Laptop": 1200,
    "Mouse": 50,
    "Keyboard": 80,
    "Monitor": 300,
    "USB Cable": 15
}

def print_expensive_products(product_dict):
    for product, price in product_dict.items():
        if price > 10:
            print(f"{product}: ${price}")

if __name__ == '__main__':
    print_expensive_products(products)