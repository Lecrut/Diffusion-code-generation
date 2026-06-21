def calculate_price(original_price, discount_percent):
    discount_amount = original_price * discount_percent / 100
    final_price = original_price - discount_amount
    return original_price, discount_amount, final_price

if __name__ == '__main__':
    original = 99.99
    discount = 30
    result = calculate_price(original, discount)
    print(result)