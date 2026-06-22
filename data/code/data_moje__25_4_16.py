from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_total(prices, discount_percent):
    discount_rate = Decimal(str(discount_percent)) / Decimal(100)
    total = Decimal(0)
    for price in prices:
        price_decimal = Decimal(str(price))
        discounted_price = price_decimal * (Decimal(1) - discount_rate)
        total += discounted_price
    return float(total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

if __name__ == '__main__':
    sample_prices = [10.0, 20.5, 30.0]
    discount = 25
    result = calculate_discounted_total(sample_prices, discount)
    print(result)