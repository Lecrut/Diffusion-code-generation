def compute_discounted_price(base_price, discount_rate=0.15):
    discount_amount = base_price * discount_rate
    return base_price - discount_amount

if __name__ == '__main__':
    value1 = compute_discounted_price(100)
    value2 = compute_discounted_price(250)
    print(value1)
    print(value2)