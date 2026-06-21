def calculate_final_cost(price, discount_rate):
    discount_amount = price * discount_rate
    final_cost = price - discount_amount
    return final_cost

if __name__ == '__main__':
    item_price = 75.50
    discount_percentage = 0.10
    result = calculate_final_cost(item_price, discount_percentage)
    print(result)