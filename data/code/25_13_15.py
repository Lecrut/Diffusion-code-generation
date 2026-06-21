def apply_discount(prices, discount_rate):
    return [price * (1 - discount_rate) for price in prices]

if __name__ == '__main__':
    sample_prices = [10.0, 25.5, 50.0, 100.0]
    discount = 0.2
    discounted_prices = apply_discount(sample_prices, discount)
    print(discounted_prices)