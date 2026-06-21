def calculate_discount(base_price, discount_rate):
    discount_amount = base_price * discount_rate
    final_price = base_price - discount_amount
    return discount_amount, final_price

if __name__ == '__main__':
    base_price = 500
    discount_rate = 0.2
    discount_amount, final_price = calculate_discount(base_price, discount_rate)
    print(discount_amount)
    print(final_price)