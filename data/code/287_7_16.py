CONVERSION_FACTOR = 1000

def calculate_total_weight(cart_items):
    total_weight_grams = sum(weight for _, weight in cart_items)
    return total_weight_grams / CONVERSION_FACTOR

if __name__ == '__main__':
    sample_cart = [('apple', 150), ('banana', 200), ('orange', 300)]
    print(calculate_total_weight(sample_cart))