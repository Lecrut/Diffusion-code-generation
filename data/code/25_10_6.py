def compute_discount_and_final_price(price, discount_rate):
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    return discount_amount, final_price

if __name__ == '__main__':
    price = 100.0
    discount_rate = 0.2
    result = compute_discount_and_final_price(price, discount_rate)
    print(result)