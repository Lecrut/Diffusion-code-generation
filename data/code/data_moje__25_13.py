def apply_discount(prices, discount_rate):
    return [price * (1 - discount_rate) for price in prices]

if __name__ == '__main__':
    sample_prices = [10.0, 20.0, 30.0, 40.0, 50.0]
    discount = 0.15
    discounted_prices = apply_discount(sample_prices, discount)
    print(discounted_prices)