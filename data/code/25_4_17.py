from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_total(prices, discount_percent):
    decimal_prices = [Decimal(str(p)) for p in prices]
    discount_factor = Decimal('1') - Decimal(str(discount_percent)) / Decimal('100')
    discounted_prices = [price * discount_factor for price in decimal_prices]
    total = sum(discounted_prices)
    return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    prices = [10.0, 20.5, 30.0]
    discount = 25
    result = calculate_discounted_total(prices, discount)
    print(result)