def calculate_final_price(base_price: float, discount_percentage: float) -> float:
    if base_price < 0:
        raise ValueError('Base price cannot be negative')
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError('Discount percentage must be between 0 and 100')
    discount_amount = base_price * (discount_percentage / 100)
    final_price = base_price - discount_amount
    return final_price
if __name__ == '__main__':
    base = 100.0
    discount = 25.0
    result = calculate_final_price(base, discount)
    print(result)