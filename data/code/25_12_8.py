def calculate_discount(original_price, discount_percentage):
    if original_price < 0 or discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Invalid price or discount percentage")
    
    discount_value = original_price * (discount_percentage / 100)
    final_price = original_price - discount_value
    
    return {
        "original_price": original_price,
        "discount_percentage": discount_percentage,
        "discount_value": discount_value,
        "final_price": final_price
    }

if __name__ == '__main__':
    result = calculate_discount(100.0, 20)
    print(result)