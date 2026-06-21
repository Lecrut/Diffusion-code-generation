def calculate_price_details(original_price, discount_percentage):
    discount_value = original_price * (discount_percentage / 100)
    final_price = original_price - discount_value
    return {
        "original_price": original_price,
        "discount_percentage": discount_percentage,
        "calculated_discount_value": discount_value,
        "final_price": final_price
    }

if __name__ == '__main__':
    result = calculate_price_details(100.0, 20.0)
    print(result)