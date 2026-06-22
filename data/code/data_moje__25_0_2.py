import decimal

def calculate_final_price(original_price: float, discount_percent: float) -> float:
    if original_price < 0:
        raise ValueError("Original price cannot be negative")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")
    
    price_decimal = decimal.Decimal(str(original_price))
    discount_decimal = decimal.Decimal(str(discount_percent))
    hundred_decimal = decimal.Decimal('100')
    
    discount_amount = (price_decimal * discount_decimal) / hundred_decimal
    final_price = price_decimal - discount_amount
    
    return float(final_price.quantize(decimal.Decimal('0.01')))

if __name__ == '__main__':
    sample_price = 199.99
    sample_discount = 25.5
    result = calculate_final_price(sample_price, sample_discount)
    print(f"{sample_price} - {sample_discount}% = {result}")
    print(f"{calculate_final_price(1000, 10)}")
    print(f"{calculate_final_price(50.00, 0)}")
    print(f"{calculate_final_price(200.50, 100)}")