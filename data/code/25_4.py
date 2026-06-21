from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_total(prices, discount_percent):
    discount_factor = Decimal(str(discount_percent)) / Decimal('100')
    subtotal = Decimal('0')
    for price in prices:
        price_decimal = Decimal(str(price))
        discount_amount = price_decimal * discount_factor
        discounted_price = price_decimal - discount_amount
        subtotal += discounted_price
    return float(subtotal.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

if __name__ == '__main__':
    prices = [10.0, 20.5, 30.0]
    discount = 25
    result = calculate_discounted_total(prices, discount)
    print(result)