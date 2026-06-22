from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_total(prices: list[float], discount_percentage: float) -> Decimal:
    discount_factor = Decimal('1') - Decimal(str(discount_percentage / 100))
    total = Decimal('0')
    for price in prices:
        total += Decimal(str(price)) * discount_factor
    return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    prices = [10.0, 20.5, 30.0]
    discount_percentage = 25
    result = calculate_discounted_total(prices, discount_percentage)
    print(result)