def compute_discounted_price(original_price):
    discount_rate = 0.15
    discounted_price = original_price * (1 - discount_rate)
    return discounted_price

if __name__ == '__main__':
    sample_values = [100, 250]
    for value in sample_values:
        result = compute_discounted_price(value)
        print(result)