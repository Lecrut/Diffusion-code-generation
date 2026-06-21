def apply_discount(prices, discount_rate):
    return [price * (1 - discount_rate) for price in prices]

if __name__ == '__main__':
    sample_prices = [100, 200, 300, 400, 500]
    discount = 0.2
    result = apply_discount(sample_prices, discount)
    print(result)