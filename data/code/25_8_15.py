def calculate_final_price(original_price: float) -> float:
    discount_rate: float = 0.4
    final_price: float = original_price * (1 - discount_rate)
    return final_price

if __name__ == '__main__':
    initial_amount: float = 200
    result: float = calculate_final_price(initial_amount)
    print(result)