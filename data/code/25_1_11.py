def compute_discounted_price(price):
    discount_rate = 0.15
    discount_amount = price * discount_rate
    return price - discount_amount

if __name__ == '__main__':
    print(compute_discounted_price(100))
    print(compute_discounted_price(250))