def calculate_final_cost(original_price, discount_percentage):
    discount_amount = original_price * (discount_percentage / 100)
    final_cost = original_price - discount_amount
    return final_cost

if __name__ == '__main__':
    item_price = 75.50
    discount = 10
    result = calculate_final_cost(item_price, discount)
    print(result)