def calculate_final_price(original_price, discount_percentage):
    if not isinstance(original_price, (int, float)) or not isinstance(discount_percentage, (int, float)):
        raise TypeError("Both arguments must be numeric")
    if original_price < 0 or discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Invalid price or discount percentage")
    discount_amount = original_price * (discount_percentage / 100)
    return original_price - discount_amount

if __name__ == '__main__':
    original_price_value = 100.0
    discount_percentage_value = 20.0
    result = calculate_final_price(original_price_value, discount_percentage_value)
    print(result)