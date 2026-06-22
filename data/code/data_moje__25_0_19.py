def calculate_final_price(original_price, discount_percentage):
    if not isinstance(original_price, (int, float)):
        raise TypeError("original_price must be a number")
    if not isinstance(discount_percentage, (int, float)):
        raise TypeError("discount_percentage must be a number")
    if original_price < 0:
        raise ValueError("original_price cannot be negative")
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("discount_percentage must be between 0 and 100")
    
    discount_multiplier = 1 - discount_percentage / 100
    final_price = original_price * discount_multiplier
    return round(final_price, 2)

if __name__ == '__main__':
    original = 100.00
    discount = 20
    result = calculate_final_price(original, discount)
    print(result)