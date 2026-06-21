def calculate_discount(original_price, discount_percentage):
    discount_amount = original_price * (discount_percentage / 100)
    final_price = original_price - discount_amount
    return original_price, discount_amount, final_price

if __name__ == '__main__':
    original_price = 99.99
    discount_percentage = 30
    result = calculate_discount(original_price, discount_percentage)
    print(result)