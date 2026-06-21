def apply_discount(values, rate):
    return [value * (1 - rate) for value in values]

if __name__ == '__main__':
    prices = [100, 200, 300]
    discount_rate = 0.05
    discounted_prices = apply_discount(prices, discount_rate)
    print(discounted_prices)