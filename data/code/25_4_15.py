from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_total(prices, discount_percentage):
    prices_decimal = [Decimal(str(p)) for p in prices]
    discount_factor = Decimal(str(discount_percentage)) / Decimal('100')
    discounted_prices = [price * (Decimal('1') - discount_factor) for price in prices_decimal]
    total = sum(discounted_prices)
    return float(total)

if __name__ == '__main__':
    prices = [10.0, 20.5, 30.0]
    discount = 25
    result = calculate_discounted_total(prices, discount)
    print(result)