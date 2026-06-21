def compute_discounted_price(price):
    discount_rate = 0.15
    return price * (1 - discount_rate)

if __name__ == '__main__':
    value1 = 100
    value2 = 250
    print(compute_discounted_price(value1))
    print(compute_discounted_price(value2))