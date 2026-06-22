def calculate_final_cost(original_price, discount_percent):
    discount_amount = original_price * (discount_percent / 100.0)
    return original_price - discount_amount

if __name__ == '__main__':
    item_price = 75.50
    discount_rate = 10
    final_cost = calculate_final_cost(item_price, discount_rate)
    print(final_cost)