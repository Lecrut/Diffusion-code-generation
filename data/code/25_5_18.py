def calculate_price_details(original_price, discount_percent):
    discount_amount = original_price * (discount_percent / 100.0)
    final_price = original_price - discount_amount
    return original_price, discount_amount, final_price

if __name__ == '__main__':
    original, discount, final = calculate_price_details(99.99, 30)
    print((original, discount, final))