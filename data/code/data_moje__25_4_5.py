from decimal import Decimal, getcontext

def calculate_discounted_total(prices, discount_percent):
    getcontext().prec = 28
    decimal_prices = [Decimal(str(p)) for p in prices]
    discount_factor = Decimal(str(discount_percent)) / Decimal('100')
    discounted_prices = [price * (Decimal('1') - discount_factor) for price in decimal_prices]
    total = sum(discounted_prices)
    return float(total)

if __name__ == '__main__':
    prices = [10.0, 20.5, 30.0]
    discount = 25
    result = calculate_discounted_total(prices, discount)
    print(result)