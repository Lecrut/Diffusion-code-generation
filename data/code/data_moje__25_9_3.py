def calculate_final_price(price: float, discount_percent: float) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative")
    if discount_percent < 0:
        raise ValueError("Discount cannot be negative")
    if discount_percent > 100:
        raise ValueError("Discount cannot exceed 100%")
    discount_amount = price * (discount_percent / 100.0)
    final_price = price - discount_amount
    return final_price

if __name__ == "__main__":
    sample_price = 100.0
    sample_discount = 20.0
    result = calculate_final_price(sample_price, sample_discount)
    print(result)