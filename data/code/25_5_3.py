def calculate_price(original_price, discount_percent):
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    return (original_price, discount_amount, final_price)

if __name__ == '__main__':
    original, discount, final = calculate_price(99.99, 30)
    print((original, discount, final))