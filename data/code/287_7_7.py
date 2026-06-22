def calculate_total_weight(cart_items):
    total_weight_grams = sum(item[1] for item in cart_items)
    return total_weight_grams / 1000

if __name__ == '__main__':
    sample_cart = [('apple', 250), ('banana', 300), ('orange', 400)]
    print(calculate_total_weight(sample_cart))