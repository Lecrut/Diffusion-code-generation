def calculate_total_weight(cart):
    return sum(weight for _, weight in cart) / 1000

if __name__ == '__main__':
    shopping_cart = [
        ("apple", 200),
        ("banana", 150),
        ("orange", 300)
    ]
    print(calculate_total_weight(shopping_cart))