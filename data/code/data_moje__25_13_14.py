def apply_discount(prices, discount_rate):
    return [price * (1 - discount_rate) for price in prices]

if __name__ == '__main__':
    sample_prices = [100.0, 200.50, 50.25, 300.00]
    fixed_discount = 0.15
    discounted_prices = apply_discount(sample_prices, fixed_discount)
    print(discounted_prices)