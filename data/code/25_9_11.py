def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    if original_price < 0:
        raise ValueError("Original price cannot be negative.")
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100 inclusive.")
    
    discount_amount = original_price * (discount_percentage / 100)
    final_price = original_price - discount_amount
    return final_price

if __name__ == '__main__':
    original_price = 100.0
    discount_percent = 20.0
    result = calculate_discounted_price(original_price, discount_percent)
    print(result)