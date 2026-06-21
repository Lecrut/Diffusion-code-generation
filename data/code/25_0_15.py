def calculate_final_price(original_price, discount_percentage):
    if not isinstance(original_price, (int, float)):
        raise TypeError("Original price must be a number")
    if not isinstance(discount_percentage, (int, float)):
        raise TypeError("Discount percentage must be a number")
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    discount_amount = original_price * (discount_percentage / 100)
    return original_price - discount_amount

if __name__ == '__main__':
    original = 150.0
    discount = 20.0
    result = calculate_final_price(original, discount)
    print(result)