def calculate_total_weight(cart):
    total_weight_grams = sum(weight for _, weight in cart)
    return total_weight_grams / 1000

if __name__ == '__main__':
    sample_cart = [('apple', 150), ('banana', 200), ('orange', 300)]
    print(calculate_total_weight(sample_cart))