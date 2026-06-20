def calculate_monetary_difference(value1, value2):
    from decimal import Decimal
    return Decimal(str(value1)) - Decimal(str(value2))

if __name__ == '__main__':
    result = calculate_monetary_difference(10.50, 3.25)
    print(result)