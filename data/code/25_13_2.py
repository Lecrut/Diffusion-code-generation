def apply_discount(prices, discount_rate):
    return [price * (1 - discount_rate) for price in prices]

if __name__ == '__main__':
    original_prices = [100, 200, 150, 300, 50]
    discount = 0.2
    discounted_prices = apply_discount(original_prices, discount)
    print(discounted_prices)