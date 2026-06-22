import decimal

UNIT_CONVERSION_FACTOR = decimal.Decimal('1000')

def convert_distance(input_decimal):
    kilometers = decimal.Decimal(str(input_decimal))
    meters = kilometers * UNIT_CONVERSION_FACTOR
    return meters

if __name__ == '__main__':
    sample_km = 9876.543210987654321
    output_meters = convert_distance(sample_km)
    print(output_meters)