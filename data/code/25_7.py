def compute_discounted_prices(prices, discount_rate):
    results = []
    for price in prices:
        discounted = price * (1 - discount_rate)
        results.append(discounted)
    return results

if __name__ == '__main__':
    values = [100, 200, 300]
    rate = 0.05
    final_prices = compute_discounted_prices(values, rate)
    print(final_prices)