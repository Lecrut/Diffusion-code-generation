def calculate_discount(original_price, discount_rate):
    discount_amount = original_price * discount_rate / 100.0
    final_price = original_price - discount_amount
    return original_price, discount_amount, final_price

if __name__ == '__main__':
    original_price = 99.99
    discount_rate = 30.0
    result = calculate_discount(original_price, discount_rate)
    print(result)