def compute_discounted_prices(values, discount_rate):
    return [v * (1 - discount_rate) for v in values]

if __name__ == '__main__':
    prices = [100, 200, 300]
    rate = 0.05
    result = compute_discounted_prices(prices, rate)
    print(result)