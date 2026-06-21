def calculate_discounted_price(original_price, discount_percentage):
    discount_amount = original_price * (discount_percentage / 100)
    final_price = original_price - discount_amount
    return original_price, discount_amount, final_price

if __name__ == '__main__':
    result = calculate_discounted_price(99.99, 30)
    print(result)