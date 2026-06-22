def calculate_total_weight(cart):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in cart):
        raise ValueError("Cart items must be tuples of (item_name, weight_in_grams)")
    total_weight_grams = sum(weight for _, weight in cart)
    return total_weight_grams / 1000

if __name__ == '__main__':
    shopping_cart = [
        ("apple", 200),
        ("banana", 150),
        ("orange", 300)
    ]
    print(calculate_total_weight(shopping_cart))