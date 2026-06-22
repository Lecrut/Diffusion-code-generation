def calculate_discount(original_price, discount_percent):
    discount_amount = original_price * discount_percent / 100
    final_price = original_price - discount_amount
    return original_price, discount_amount, final_price

if __name__ == '__main__':
    result = calculate_discount(99.99, 30)
    print(result)