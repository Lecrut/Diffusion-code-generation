def calculate_discount(price, discount_rate):
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    return discount_amount, final_price

if __name__ == '__main__':
    hard_coded_price = 100.0
    hard_coded_discount_rate = 0.2
    amount, total = calculate_discount(hard_coded_price, hard_coded_discount_rate)
    print(amount)
    print(total)