def calculate_discounted_price(original_price: float, discount_rate: float = 0.4) -> float:
    return original_price * (1.0 - discount_rate)

if __name__ == '__main__':
    sample_price = 200.0
    result = calculate_discounted_price(sample_price)
    print(result)