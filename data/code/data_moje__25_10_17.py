def calculate_discount(price, discount_rate):
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    return discount_amount, final_price

if __name__ == '__main__':
    sample_price = 100.00
    sample_discount_rate = 0.20
    result = calculate_discount(sample_price, sample_discount_rate)
    print(result)