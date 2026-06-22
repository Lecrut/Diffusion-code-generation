def calculate_final_cost(item_price, discount_rate):
    return item_price * (1 - discount_rate)

if __name__ == '__main__':
    price = 75.50
    discount = 0.10
    final_cost = calculate_final_cost(price, discount)
    print(final_cost)