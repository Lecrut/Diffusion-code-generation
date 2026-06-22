from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_total(prices, discount_percent):
    discount_factor = Decimal(1) - Decimal(discount_percent) / Decimal(100)
    total = Decimal(0)
    for price in prices:
        price_decimal = Decimal(str(price))
        discounted_price = price_decimal * discount_factor
        total += discounted_price
    return float(total)
if __name__ == '__main__':
    prices = [10.0, 20.5, 30.0]
    discount = 25
    result = calculate_discounted_total(prices, discount)
    print(result)