from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_total(prices, discount_percent):
    total = Decimal('0')
    discount_factor = Decimal(str(100 - discount_percent)) / Decimal('100')
    for price in prices:
        price_decimal = Decimal(str(price))
        discounted_price = (price_decimal * discount_factor).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        total += discounted_price
    return float(total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

if __name__ == '__main__':
    sample_prices = [10.0, 20.5, 30.0]
    discount_rate = 25
    result = calculate_discounted_total(sample_prices, discount_rate)
    print(result)