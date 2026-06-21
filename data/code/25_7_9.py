def compute_discounted_prices(prices, discount_rate):
    return [price * (1 - discount_rate) for price in prices]

if __name__ == '__main__':
    hard_coded_prices = [100, 200, 300]
    discount_rate = 0.05
    discounted_prices = compute_discounted_prices(hard_coded_prices, discount_rate)
    print(discounted_prices)