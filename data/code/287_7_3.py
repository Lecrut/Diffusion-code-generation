def calculate_total_weight(cart):
    total_weight_grams = sum(weight for _, weight in cart)
    return total_weight_grams / 1000

if __name__ == '__main__':
    shopping_cart = [
        ("Apple", 150),
        ("Banana", 120),
        ("Cherry", 300)
    ]
    print(calculate_total_weight(shopping_cart))