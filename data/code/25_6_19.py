def calculate_discounted_price(price: float, discount_percentage: float) -> float:
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    return final_price

if __name__ == '__main__':
    item_price = 75.50
    discount_rate = 10.0
    result = calculate_discounted_price(item_price, discount_rate)
    print(result)