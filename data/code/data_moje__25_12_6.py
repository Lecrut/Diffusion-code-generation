def calculate_discount(price, discount_percentage):
    discount_value = price * (discount_percentage / 100)
    final_price = price - discount_value
    return {
        "original_price": price,
        "discount_percentage": discount_percentage,
        "discount_value": discount_value,
        "final_price": final_price
    }

if __name__ == '__main__':
    original = 100
    discount = 20
    result = calculate_discount(original, discount)
    print(result)