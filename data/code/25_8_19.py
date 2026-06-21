def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    discount_amount: float = original_price * (discount_percentage / 100.0)
    final_price: float = original_price - discount_amount
    return final_price

if __name__ == '__main__':
    original_price: float = 200.0
    discount_percentage: float = 40.0
    result: float = calculate_discounted_price(original_price, discount_percentage)
    print(result)