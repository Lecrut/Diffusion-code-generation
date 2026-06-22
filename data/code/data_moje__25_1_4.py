def compute_discounted_price(price):
    discount_rate = 0.15
    discount_amount = price * discount_rate
    return price - discount_amount

if __name__ == '__main__':
    sample_price_1 = 100
    sample_price_2 = 250
    result_1 = compute_discounted_price(sample_price_1)
    result_2 = compute_discounted_price(sample_price_2)
    print(result_1)
    print(result_2)