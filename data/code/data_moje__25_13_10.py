def apply_discount(prices, discount_rate):
    return [price * (1 - discount_rate) for price in prices]

if __name__ == '__main__':
    sample_prices = [100.0, 200.5, 50.25, 75.0]
    discount = 0.2
    discounted_prices = apply_discount(sample_prices, discount)
    print(discounted_prices)