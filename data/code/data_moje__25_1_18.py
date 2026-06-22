def compute_discounted_price(price):
    discount_rate = 0.15
    return price * (1 - discount_rate)

if __name__ == '__main__':
    sample_prices = [100, 250]
    for price in sample_prices:
        discounted = compute_discounted_price(price)
        print(discounted)