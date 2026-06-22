def calculate_discounted_price(price: float, discount_percentage: float) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative")
    if discount_percentage < 0:
        raise ValueError("Discount percentage cannot be negative")
    if discount_percentage > 100:
        raise ValueError("Discount percentage cannot exceed 100%")
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    return round(final_price, 2)

if __name__ == '__main__':
    sample_price = 100.0
    sample_discount = 20.0
    result = calculate_discounted_price(sample_price, sample_discount)
    print(result)