def apply_discount(prices, rate):
    return [price * (1 - rate) for price in prices]

if __name__ == '__main__':
    values = [100, 200, 300]
    discount_rate = 0.05
    result = apply_discount(values, discount_rate)
    print(result)