def calculate_discounted_price(original_price: float) -> float:
    discount_rate: float = 0.4
    return original_price * (1 - discount_rate)

if __name__ == "__main__":
    input_value: int = 200
    result: float = calculate_discounted_price(input_value)
    print(result)