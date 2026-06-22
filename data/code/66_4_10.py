from decimal import Decimal, ROUND_HALF_UP

def km_to_m(kilometers):
    km_decimal = Decimal(str(kilometers))
    meters_decimal = km_decimal * 1000
    rounded_meters = meters_decimal.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    return float(rounded_meters)

if __name__ == '__main__':
    sample_values = [1.0, 0.1, 1.005, 10.5, 100.123456]
    for val in sample_values:
        result = km_to_m(val)
        print(result)