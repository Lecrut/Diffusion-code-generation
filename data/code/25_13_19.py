def apply_discount(prices: list[float], discount_rate: float) -> list[float]:
    return [price * (1 - discount_rate) for price in prices]

if __name__ == '__main__':
    sample_prices = [100.0, 200.0, 300.0]
    discount = 0.1
    result = apply_discount(sample_prices, discount)
    print(result)