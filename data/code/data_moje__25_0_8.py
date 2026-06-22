def apply_discount(original_price: float, discount_percent: float) -> float:
    if original_price < 0:
        raise ValueError("Original price cannot be negative")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    discount_multiplier = 1.0 - (discount_percent / 100.0)
    return original_price * discount_multiplier

if __name__ == "__main__":
    sample_price = 100.0
    sample_discount = 25.0
    final_price = apply_discount(sample_price, sample_discount)
    print(final_price)