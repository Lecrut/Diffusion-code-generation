def calculate_final_cost(price, discount_rate):
    discount_amount = price * discount_rate
    return price - discount_amount

if __name__ == '__main__':
    item_price = 75.50
    discount_rate = 0.10
    final_cost = calculate_final_cost(item_price, discount_rate)
    print(final_cost)