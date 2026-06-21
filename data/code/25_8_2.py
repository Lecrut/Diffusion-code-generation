def calculate_discounted_price(original_price: float) -> float:
    discount_rate: float = 0.4
    discounted_price: float = original_price * (1 - discount_rate)
    return discounted_price

if __name__ == '__main__':
    sample_price: float = 200
    result: float = calculate_discounted_price(sample_price)
    print(result)