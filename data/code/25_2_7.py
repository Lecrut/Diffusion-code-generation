def calculate_discount(base_price, discount_percentage):
    savings = base_price * discount_percentage / 100
    final_price = base_price - savings
    return savings, final_price

if __name__ == '__main__':
    base_price = 500
    discount_percentage = 20
    savings, final_price = calculate_discount(base_price, discount_percentage)
    print(savings)
    print(final_price)