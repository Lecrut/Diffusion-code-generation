from decimal import Decimal

def calculate_monetary_difference(value1, value2):
    return Decimal(str(value1)) - Decimal(str(value2))

if __name__ == '__main__':
    amount_a = 50.75
    amount_b = 17.99
    result = calculate_monetary_difference(amount_a, amount_b)
    print(result)