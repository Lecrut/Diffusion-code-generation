def calculate_discounted_price(original_price, discount_percentage):
    if not isinstance(original_price, (int, float)):
        raise TypeError("original_price must be a number")
    if not isinstance(discount_percentage, (int, float)):
        raise TypeError("discount_percentage must be a number")
    if original_price < 0:
        raise ValueError("original_price cannot be negative")
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("discount_percentage must be between 0 and 100")
    discount_factor = 1 - (discount_percentage / 100)
    final_price = original_price * discount_factor
    return final_price

if __name__ == '__main__':
    original_price = 100.0
    discount_percentage = 20.0
    result = calculate_discounted_price(original_price, discount_percentage)
    print(result)