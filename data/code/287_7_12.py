CONVERSION_FACTOR = 1000

def calculate_total_weight(cart_items):
    total_weight_grams = sum(item[1] for item in cart_items)
    return total_weight_grams / CONVERSION_FACTOR

if __name__ == '__main__':
    shopping_cart = [
        ("apple", 200),
        ("banana", 150),
        ("orange", 300)
    ]
    print(calculate_total_weight(shopping_cart))