def calculate_discounted_price(original_price, discount_percentage):
    discount_value = original_price * (discount_percentage / 100)
    final_price = original_price - discount_value
    return {
        'original_price': original_price,
        'discount_percentage': discount_percentage,
        'discount_value': discount_value,
        'final_price': final_price
    }

if __name__ == '__main__':
    sample_original_price = 100.0
    sample_discount_percentage = 20.0
    result = calculate_discounted_price(sample_original_price, sample_discount_percentage)
    print(result)