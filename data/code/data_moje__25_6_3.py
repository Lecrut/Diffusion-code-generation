def calculate_final_cost(price, discount_percentage):
    discount_amount = price * (discount_percentage / 100.0)
    final_cost = price - discount_amount
    return final_cost

if __name__ == '__main__':
    item_price = 75.50
    discount = 10.0
    result = calculate_final_cost(item_price, discount)
    print(result)