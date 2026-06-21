def calculate_prices(original_price, discount_percent):
    discount_amount = original_price * discount_percent / 100
    final_price = original_price - discount_amount
    return original_price, discount_amount, final_price

if __name__ == '__main__':
    original = 99.99
    discount_rate = 30
    result = calculate_prices(original, discount_rate)
    print(result)