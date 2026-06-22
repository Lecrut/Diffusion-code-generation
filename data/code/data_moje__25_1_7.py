def calculate_discounted_price(original_price):
    discount_rate = 0.15
    discount_amount = original_price * discount_rate
    discounted_price = original_price - discount_amount
    return discounted_price

if __name__ == '__main__':
    price_1 = 100
    price_2 = 250
    result_1 = calculate_discounted_price(price_1)
    result_2 = calculate_discounted_price(price_2)
    print(result_1)
    print(result_2)