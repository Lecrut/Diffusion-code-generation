import decimal

def calculate_discounted_total(prices, discount_rate):
    total = decimal.Decimal('0')
    discount_factor = decimal.Decimal('1') - decimal.Decimal(str(discount_rate))
    for price in prices:
        total += decimal.Decimal(str(price)) * discount_factor
    return float(total)

if __name__ == '__main__':
    prices = [10.0, 20.5, 30.0]
    discount_rate = 0.25
    result = calculate_discounted_total(prices, discount_rate)
    print(result)