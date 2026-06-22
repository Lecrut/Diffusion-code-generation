def calculate_discount(base_price, discount_percent):
    discount_amount = base_price * (discount_percent / 100)
    final_price = base_price - discount_amount
    return discount_amount, final_price

if __name__ == '__main__':
    base_price = 500
    discount_percent = 20
    savings, final_price = calculate_discount(base_price, discount_percent)
    print(f"Savings: {savings}")
    print(f"Final Price: {final_price}")