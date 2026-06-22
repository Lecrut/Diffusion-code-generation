def compute_discounted_total(unit_price):
    base = float(unit_price)
    threshold = 100.0
    high_rate = 0.90
    low_rate = 0.95
    multiplier = high_rate if base > threshold else low_rate
    final_total = base * multiplier
    return final_total

if __name__ == '__main__':
    test_price_a = 50
    test_price_b = 150
    value_a = compute_discounted_total(test_price_a)
    value_b = compute_discounted_total(test_price_b)
    print(value_a)
    print(value_b)