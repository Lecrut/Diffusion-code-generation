def apply_discount(values, rate):
    if not values:
        return []
    factor = 1 - rate
    return [v * factor for v in values]

if __name__ == '__main__':
    prices = [100, 200, 300]
    discount_rate = 0.05
    result = apply_discount(prices, discount_rate)
    print(result)