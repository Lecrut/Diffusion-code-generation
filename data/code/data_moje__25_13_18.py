def apply_fixed_discount(prices, discount_rate):
    return [price * (1 - discount_rate) for price in prices]

if __name__ == '__main__':
    sample_prices = [100.0, 200.50, 350.75, 50.00]
    discount = 0.20
    discounted_prices = apply_fixed_discount(sample_prices, discount)
    print(discounted_prices)