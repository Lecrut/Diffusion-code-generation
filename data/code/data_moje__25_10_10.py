def compute_discount(price, discount_rate):
    if price < 0 or discount_rate < 0 or discount_rate > 1:
        return 0, price
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    return discount_amount, final_price

if __name__ == '__main__':
    price = 100
    discount_rate = 0.15
    discount, final = compute_discount(price, discount_rate)
    print(discount)
    print(final)