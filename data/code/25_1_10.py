def compute_discounted_price(original_price, discount_rate=0.15):
    return original_price * (1 - discount_rate)

if __name__ == '__main__':
    print(compute_discounted_price(100))
    print(compute_discounted_price(250))