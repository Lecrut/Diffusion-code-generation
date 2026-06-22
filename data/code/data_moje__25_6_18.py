def calculate_discounted_price(base_price, discount_rate):
    discount_amount = base_price * discount_rate
    final_cost = base_price - discount_amount
    return final_cost

if __name__ == '__main__':
    item_price = 75.50
    discount_rate = 0.10
    result = calculate_discounted_price(item_price, discount_rate)
    print(result)