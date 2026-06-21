def calculate_final_price(price: float, discount_percentage: float) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative")
    if discount_percentage < 0:
        raise ValueError("Discount percentage cannot be negative")
    if discount_percentage > 100:
        raise ValueError("Discount percentage cannot exceed 100%")
    
    discount_amount = price * (discount_percentage / 100.0)
    return price - discount_amount

if __name__ == '__main__':
    sample_price = 100.0
    sample_discount = 20.0
    result = calculate_final_price(sample_price, sample_discount)
    print(result)
    
    try:
        calculate_final_price(-50.0, 10.0)
    except ValueError as e:
        print(e)
        
    try:
        calculate_final_price(50.0, 150.0)
    except ValueError as e:
        print(e)