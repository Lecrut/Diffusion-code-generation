def calculate_discount_and_final_price(price, discount_rate):
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    return discount_amount, final_price

if __name__ == '__main__':
    sample_price = 100
    sample_discount_rate = 0.2
    discount_result, final_result = calculate_discount_and_final_price(sample_price, sample_discount_rate)
    print(discount_result)
    print(final_result)