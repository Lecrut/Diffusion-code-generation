def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    if original_price < 0:
        raise ValueError("Original price cannot be negative")
    if discount_percentage < 0:
        raise ValueError("Discount percentage cannot be negative")
    if discount_percentage > 100:
        raise ValueError("Discount percentage cannot exceed 100")
    
    discount_amount = original_price * (discount_percentage / 100)
    final_price = original_price - discount_amount
    
    return round(final_price, 2)

if __name__ == '__main__':
    print(calculate_discounted_price(100, 20))
    print(calculate_discounted_price(50, 50))
    print(calculate_discounted_price(200, 0))
    print(calculate_discounted_price(99.99, 15))