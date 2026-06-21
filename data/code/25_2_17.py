def calculate_savings_and_price(base_price, discount_percent):
    discount_amount = base_price * discount_percent / 100
    final_price = base_price - discount_amount
    return discount_amount, final_price

if __name__ == '__main__':
    base = 500
    discount = 20
    savings, final_cost = calculate_savings_and_price(base, discount)
    print(savings)
    print(final_cost)