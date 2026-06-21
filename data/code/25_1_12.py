def compute_discounted_price(original_price, discount_rate=0.15):
    return original_price * (1 - discount_rate)

if __name__ == '__main__':
    sample_values = [100, 250]
    for value in sample_values:
        print(compute_discounted_price(value))