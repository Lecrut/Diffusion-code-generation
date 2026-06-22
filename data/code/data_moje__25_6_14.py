def calculate_final_cost(original_price, discount_rate):
    discount_amount = original_price * discount_rate
    final_cost = original_price - discount_amount
    return final_cost

if __name__ == '__main__':
    original_price = 75.50
    discount_rate = 0.1
    final_cost = calculate_final_cost(original_price, discount_rate)
    print(final_cost)