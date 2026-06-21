def compute_discounted_prices(prices, discount_rate):
    return [p * (1 - discount_rate) for p in prices]

if __name__ == '__main__':
    prices = [100, 200, 300]
    discount_rate = 0.05
    result = compute_discounted_prices(prices, discount_rate)
    print(result)