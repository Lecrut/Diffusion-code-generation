def calculate_discounted_cost(price, discount_rate):
    return price * (1 - discount_rate)

if __name__ == '__main__':
    item_price = 75.50
    discount = 0.10
    final_cost = calculate_discounted_cost(item_price, discount)
    print(final_cost)