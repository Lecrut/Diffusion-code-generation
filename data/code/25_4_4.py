import decimal

def calculate_discounted_total(prices, discount_rate):
    decimal.getcontext().prec = 28
    discount_factor = decimal.Decimal('1') - decimal.Decimal(str(discount_rate))
    total = decimal.Decimal('0')
    for price in prices:
        price_decimal = decimal.Decimal(str(price))
        discounted_price = price_decimal * discount_factor
        total += discounted_price
    return total

if __name__ == '__main__':
    prices = [10.0, 20.5, 30.0]
    discount_rate = 0.25
    result = calculate_discounted_total(prices, discount_rate)
    print(result)