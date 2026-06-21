def calculate_final_price(original_price, discount_percentage):
    if not isinstance(original_price, (int, float)):
        raise TypeError("original_price must be a number")
    if not isinstance(discount_percentage, (int, float)):
        raise TypeError("discount_percentage must be a number")
    if original_price < 0:
        raise ValueError("original_price must be non-negative")
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("discount_percentage must be between 0 and 100")
    final_price = original_price * (1 - discount_percentage / 100)
    return round(final_price, 2)

if __name__ == '__main__':
    print(calculate_final_price(100, 20))
    print(calculate_final_price(250.50, 15))
    print(calculate_final_price(99.99, 0))
    print(calculate_final_price(50, 100))