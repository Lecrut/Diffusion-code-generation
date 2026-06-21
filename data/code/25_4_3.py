from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_total(prices, discount_percent):
    discount_rate = Decimal(discount_percent) / Decimal('100')
    discounted_prices = []
    for price in prices:
        original_price = Decimal(str(price))
        discounted_price = original_price * (Decimal('1') - discount_rate)
        discounted_prices.append(discounted_price)
    total = sum(discounted_prices)
    return total
if __name__ == '__main__':
    prices = [10.0, 20.5, 30.0]
    discount = 25
    result = calculate_discounted_total(prices, discount)
    print(result)