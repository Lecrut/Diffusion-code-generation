def compute_discounted_price(original_price):
    discount_rate = 0.15
    return original_price * (1 - discount_rate)

if __name__ == '__main__':
    value_1 = 100
    value_2 = 250
    result_1 = compute_discounted_price(value_1)
    result_2 = compute_discounted_price(value_2)
    print(result_1)
    print(result_2)