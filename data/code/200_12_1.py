def calculate_total_price(products):
    total_price = 0
    for product in products:
        total_price += product.get("price", 0)
    return total_price
if __name__ == '__main__':
    product_list = [
        {"name": "Laptop", "price": 1200.50, "quantity": 1},
        {"name": "Mouse", "price": 25.99, "quantity": 2},
        {"name": "Keyboard", "price": 75.00, "quantity": 1},
        {"name": "Monitor", "price": 350.75, "quantity": 1}
    ]
    total = calculate_total_price(product_list)
    print(total)