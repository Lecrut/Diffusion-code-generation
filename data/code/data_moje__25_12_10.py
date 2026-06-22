def calculate_discounted_price(original_price, discount_percentage):
    discount_value = original_price * (discount_percentage / 100)
    final_price = original_price - discount_value
    return {
        "original_price": original_price,
        "discount_percentage": discount_percentage,
        "discount_value": discount_value,
        "final_price": final_price
    }

if __name__ == '__main__':
    result = calculate_discounted_price(100, 20)
    print(result)