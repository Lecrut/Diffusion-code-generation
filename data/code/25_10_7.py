def calculate_discount(price, discount_rate):
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    return discount_amount, final_price

if __name__ == '__main__':
    result = calculate_discount(100.0, 0.1)
    print(result)