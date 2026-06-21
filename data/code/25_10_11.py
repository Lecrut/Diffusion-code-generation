DISCOUNT_RATE = 0.10
BASE_PRICE = 50.0

def compute_discount_data(base_price, rate):
    if rate >= 1.0:
        return 0, base_price
    if rate < 0:
        return 0, base_price
    discount = base_price * rate
    final = base_price - discount
    return discount, final

if __name__ == '__main__':
    discount_amt, final_price = compute_discount_data(BASE_PRICE, DISCOUNT_RATE)
    print(discount_amt)
    print(final_price)