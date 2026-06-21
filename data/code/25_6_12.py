def calculate_final_cost(price: float, discount_rate: float) -> float:
    discount_amount = price * discount_rate
    final_cost = price - discount_amount
    return final_cost

if __name__ == '__main__':
    item_price = 75.50
    discount_rate = 0.10
    result = calculate_final_cost(item_price, discount_rate)
    print(result)