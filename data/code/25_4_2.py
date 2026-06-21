from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_total(prices, discount_percent):
    total = Decimal('0')
    for price in prices:
        price_val = Decimal(str(price))
        discount_rate = Decimal(str(discount_percent)) / Decimal('100')
        discounted_price = price_val * (Decimal('1') - discount_rate)
        total += discounted_price
    return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    prices_list = [10.0, 20.5, 30.0]
    discount_percent = 25
    result = calculate_discounted_total(prices_list, discount_percent)
    print(result)