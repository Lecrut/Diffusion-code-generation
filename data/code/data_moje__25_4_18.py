from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_total(prices, discount_percent):
    total = Decimal('0')
    discount_factor = Decimal('1') - Decimal(str(discount_percent / 100))
    for price in prices:
        total += Decimal(str(price))
    discounted_total = total * discount_factor
    return float(discounted_total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

if __name__ == '__main__':
    prices = [10.0, 20.5, 30.0]
    discount_percent = 25
    result = calculate_discounted_total(prices, discount_percent)
    print(result)