import decimal

def convert_kilometers_to_meters(kilometers):
    km_decimal = decimal.Decimal(str(kilometers))
    meters_decimal = km_decimal * decimal.Decimal('1000')
    return meters_decimal

if __name__ == '__main__':
    input_value = 1.23456
    result = convert_kilometers_to_meters(input_value)
    print(result)