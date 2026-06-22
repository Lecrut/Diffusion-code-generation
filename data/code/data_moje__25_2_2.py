def calculate_savings_and_final_price(base_price, discount_percent):
    savings = base_price * (discount_percent / 100)
    final_price = base_price - savings
    return savings, final_price

if __name__ == '__main__':
    base_price = 500
    discount_percent = 20
    savings, final_price = calculate_savings_and_final_price(base_price, discount_percent)
    print({"savings": savings, "final_price": final_price})