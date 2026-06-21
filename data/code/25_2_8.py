def calculate_discount(base_price, discount_rate):
    savings = base_price * discount_rate
    final_price = base_price - savings
    return savings, final_price

if __name__ == '__main__':
    base = 500
    rate = 0.2
    saved, final = calculate_discount(base, rate)
    print(saved)
    print(final)