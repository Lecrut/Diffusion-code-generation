def calculate_savings_and_final_price(base_price, discount_percentage):
    discount_amount = base_price * (discount_percentage / 100)
    final_price = base_price - discount_amount
    return discount_amount, final_price

if __name__ == '__main__':
    base_price = 500
    discount_percentage = 20
    savings, final_price = calculate_savings_and_final_price(base_price, discount_percentage)
    print(savings)
    print(final_price)