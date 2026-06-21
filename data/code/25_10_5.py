def compute_discount_and_final_price(price, discount_rate):
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    return (discount_amount, final_price)
if __name__ == '__main__':
    hardcoded_price = 100.0
    hardcoded_discount_rate = 0.15
    discount, final = compute_discount_and_final_price(hardcoded_price, hardcoded_discount_rate)
    print(discount, final)