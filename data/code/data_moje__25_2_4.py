def calculate_savings_and_price(base_price, discount_percent):
    discount_amount = base_price * (discount_percent / 100)
    final_price = base_price - discount_amount
    return discount_amount, final_price

if __name__ == '__main__':
    base = 500
    discount_rate = 20
    savings, final = calculate_savings_and_price(base, discount_rate)
    print(savings)
    print(final)