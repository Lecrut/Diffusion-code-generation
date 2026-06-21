from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_total(prices, discount_rate):
    total = Decimal('0')
    discount = Decimal(str(discount_rate)) / Decimal('100')
    for price in prices:
        decimal_price = Decimal(str(price))
        discounted_price = decimal_price * (Decimal('1') - discount)
        total += discounted_price
    return float(total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

if __name__ == '__main__':
    prices = [10.0, 20.5, 30.0]
    discount_rate = 25
    result = calculate_discounted_total(prices, discount_rate)
    print(result)