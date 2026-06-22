def apply_fixed_discount(prices, discount_rate):
    return [price * (1 - discount_rate) for price in prices]

if __name__ == '__main__':
    sample_prices = [100.0, 200.0, 300.0]
    discount_rate = 0.1
    result = apply_fixed_discount(sample_prices, discount_rate)
    print(result)