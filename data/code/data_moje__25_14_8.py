from decimal import Decimal, ROUND_HALF_UP

DISCOUNT_RATE = Decimal('0.15')
BASE_PRICE = Decimal('199.99')

def calculate_discounted_price(price, discount):
    if discount <= Decimal('0') or discount >= Decimal('1'):
        raise ValueError("Discount must be between 0 and 1")
    if price < Decimal('0'):
        raise ValueError("Price cannot be negative")
    
    discount_amount = price * discount
    discounted_price = price - discount_amount
    return discounted_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    result = calculate_discounted_price(BASE_PRICE, DISCOUNT_RATE)
    print(result)