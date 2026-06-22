def calculate_total_weight(cart_items):
    total_weight_grams = sum(item[1] for item in cart_items)
    return total_weight_grams / 1000

if __name__ == '__main__':
    sample_cart = [
        ("Mango", 180),
        ("Grapes", 50),
        ("Watermelon", 3500),
        ("Kiwi", 70)
    ]
    total_weight_kg = calculate_total_weight(sample_cart)
    print(f"Total weight: {total_weight_kg:.2f} kg")