def apply_discount(prices, discount_rate):
    return [price * (1 - discount_rate) for price in prices]

if __name__ == '__main__':
    prices = [100, 200, 300]
    discount = 0.1
    result = apply_discount(prices, discount)
    print(result)