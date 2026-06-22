def apply_discount(prices, discount_rate):
    return [price * (1 - discount_rate) for price in prices]

if __name__ == '__main__':
    sample_prices = [100, 200, 150, 300]
    discount_rate = 0.2
    discounted_prices = apply_discount(sample_prices, discount_rate)
    print(discounted_prices)