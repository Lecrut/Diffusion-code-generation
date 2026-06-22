def compute_final_price(base_price):
    discount_threshold = 100
    high_tier_discount_rate = 0.10
    low_tier_discount_rate = 0.05

    if base_price > discount_threshold:
        discount_multiplier = 1.0 - high_tier_discount_rate
    else:
        discount_multiplier = 1.0 - low_tier_discount_rate

    return base_price * discount_multiplier

if __name__ == '__main__':
    test_value_a = 75
    test_value_b = 200
    result_a = compute_final_price(test_value_a)
    result_b = compute_final_price(test_value_b)
    print(result_a)
    print(result_b)