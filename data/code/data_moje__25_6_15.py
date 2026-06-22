def calculate_final_cost(price: float, discount_percent: float) -> float:
    return price * (1 - discount_percent / 100)

if __name__ == '__main__':
    item_price = 75.50
    discount_rate = 10
    result = calculate_final_cost(item_price, discount_rate)
    print(result)