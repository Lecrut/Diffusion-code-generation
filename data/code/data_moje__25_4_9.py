from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_total(prices, discount_percentage):
    decimal_prices = [Decimal(str(p)) for p in prices]
    discount_rate = Decimal(str(discount_percentage)) / Decimal('100')
    discounted_prices = [p * (Decimal('1') - discount_rate) for p in decimal_prices]
    total = sum(discounted_prices)
    return float(total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

if __name__ == '__main__':
    sample_prices = [10.0, 20.5, 30.0]
    discount = 25
    result = calculate_discounted_total(sample_prices, discount)
    print(result)