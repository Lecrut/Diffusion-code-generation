from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_total(prices, discount_percentage):
    if not prices:
        return Decimal('0.00')
    discount_factor = Decimal('1.00') - Decimal(str(discount_percentage)) / Decimal('100.00')
    total = Decimal('0.00')
    for price in prices:
        price_decimal = Decimal(str(price))
        discounted_price = price_decimal * discount_factor
        total += discounted_price
    return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
if __name__ == '__main__':
    sample_prices = [10.0, 20.5, 30.0]
    discount = 25
    result = calculate_discounted_total(sample_prices, discount)
    print(result)