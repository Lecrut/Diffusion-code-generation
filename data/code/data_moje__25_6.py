def calculate_final_cost(item_price, discount_rate):
    discounted_price = item_price * (1 - discount_rate)
    return discounted_price

if __name__ == '__main__':
    final_cost = calculate_final_cost(75.50, 0.10)
    print(final_cost)