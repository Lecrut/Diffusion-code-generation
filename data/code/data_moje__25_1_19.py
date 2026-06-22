MULTIPLIER = 0.85

def get_discounted_price(base_price):
    if base_price < 0:
        return 0
    return base_price * MULTIPLIER

if __name__ == '__main__':
    first_val = get_discounted_price(100)
    second_val = get_discounted_price(250)
    print(first_val)
    print(second_val)