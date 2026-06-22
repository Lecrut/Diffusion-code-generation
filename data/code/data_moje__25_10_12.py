def compute_discount_and_final_price(price, discount_rate):
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    return discount_amount, final_price

if __name__ == '__main__':
    hard_coded_price = 100.0
    hard_coded_discount_rate = 0.15
    result = compute_discount_and_final_price(hard_coded_price, hard_coded_discount_rate)
    print(result)