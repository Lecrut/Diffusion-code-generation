def compute_discounted_prices(prices, discount_rate):
    return [price * (1 - discount_rate) for price in prices]

if __name__ == '__main__':
    values = [100, 200, 300]
    rate = 0.05
    results = compute_discounted_prices(values, rate)
    print(results)