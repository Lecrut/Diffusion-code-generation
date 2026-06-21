def calculate_discounted_price(original_price: float, discount_rate: float) -> float:
    return original_price * (1 - discount_rate)

if __name__ == '__main__':
    input_value: float = 200.0
    discount: float = 0.40
    final_price: float = calculate_discounted_price(input_value, discount)
    print(final_price)