def compute_discounted_price(price):
    return price * (1 - 0.15)

if __name__ == '__main__':
    print(compute_discounted_price(100))
    print(compute_discounted_price(250))