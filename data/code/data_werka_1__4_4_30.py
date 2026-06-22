import decimal

def convert_distance(distance, target_unit):
    conversion_factors = {'meters_to_kilometers': decimal.Decimal('0.001'), 'kilometers_to_meters': decimal.Decimal('1000'), 'meters_to_feet': decimal.Decimal('3.28084'), 'feet_to_meters': decimal.Decimal('0.3048')}
    if distance == 0:
        return decimal.Decimal('0')
    if target_unit == 'kilometers':
        conversion_key = 'meters_to_kilometers'
    elif target_unit == 'feet':
        conversion_key = 'meters_to_feet'
    else:
        raise ValueError('Unsupported target unit')
    converted_distance = distance * conversion_factors[conversion_key]
    return converted_distance
if __name__ == '__main__':
    sample_distance = decimal.Decimal('100')
    sample_target_unit = 'kilometers'
    try:
        result = convert_distance(sample_distance, sample_target_unit)
        print(f'{sample_distance} meters is {result} {sample_target_unit}')
    except ValueError as e:
        print(e)