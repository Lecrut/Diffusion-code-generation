def compute_discounted_prices(prices, discount_rate):
    return [p * (1 - discount_rate) for p in prices]

if __name__ == '__main__':
    result = compute_discounted_prices([100, 200, 300], 0.05)
    print(result)