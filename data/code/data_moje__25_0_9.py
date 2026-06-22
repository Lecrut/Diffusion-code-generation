def calculate_discounted_price(original_price, discount_percentage):
    if not isinstance(original_price, (int, float)) or not isinstance(discount_percentage, (int, float)):
        raise TypeError("Both original_price and discount_percentage must be numeric types.")
    if original_price < 0 or discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("original_price must be non-negative and discount_percentage must be between 0 and 100.")
    discount_amount = original_price * (discount_percentage / 100.0)
    return original_price - discount_amount

if __name__ == '__main__':
    original_price = 100
    discount_percentage = 20
    result = calculate_discounted_price(original_price, discount_percentage)
    print(result)