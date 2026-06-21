def calculate_final_price(original_price: float, discount_percent: float) -> float:
    discount_amount: float = original_price * (discount_percent / 100.0)
    final_price: float = original_price - discount_amount
    return final_price

if __name__ == '__main__':
    initial_amount: float = 200.0
    discount_rate: float = 40.0
    result: float = calculate_final_price(initial_amount, discount_rate)
    print(result)