def apply_discount(prices, discount_rate):
    return [price * (1 - discount_rate) for price in prices]

if __name__ == '__main__':
    sample_prices = [100.0, 200.0, 50.0, 75.5]
    discount = 0.1
    discounted_prices = apply_discount(sample_prices, discount)
    print(discounted_prices)