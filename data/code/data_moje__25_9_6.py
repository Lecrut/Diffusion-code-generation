def calculate_discounted_price(price: float, discount_percent: float) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative")
    if discount_percent < 0:
        raise ValueError("Discount percentage cannot be negative")
    if discount_percent > 100:
        raise ValueError("Discount percentage cannot exceed 100%")
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount

if __name__ == '__main__':
    sample_price = 100.0
    sample_discount = 25.0
    final_price = calculate_discounted_price(sample_price, sample_discount)
    print(final_price)
    try:
        calculate_discounted_price(-50.0, 10.0)
    except ValueError as e:
        print(e)
    try:
        calculate_discounted_price(50.0, 150.0)
    except ValueError as e:
        print(e)