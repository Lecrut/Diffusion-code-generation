def convert_distance(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversions = {
        ('meters', 'kilometers'): 0.001,
        ('kilometers', 'meters'): 1000,
        ('meters', 'miles'): 0.000621371,
        ('miles', 'meters'): 1609.344,
        ('kilometers', 'miles'): 0.621371,
        ('miles', 'kilometers'): 1.609344,
    }
    if from_unit == 'kilometers' and to_unit == 'miles':
        return value * 0.621371
    if from_unit == 'miles' and to_unit == 'kilometers':
        return value * 1.609344
    if from_unit == 'meters' and to_unit == 'kilometers':
        return value * 0.001
    if from_unit == 'kilometers' and to_unit == 'meters':
        return value * 1000
    if from_unit == 'meters' and to_unit == 'miles':
        return value * 0.000621371
    if from_unit == 'miles' and to_unit == 'meters':
        return value * 1609.344
    raise ValueError(f"Unsupported conversion: {from_unit} to {to_unit}")

if __name__ == '__main__':
    result = convert_distance(1000, 'meters', 'kilometers')
    print(result)
    result2 = convert_distance(5, 'miles', 'kilometers')
    print(result2)
    result3 = convert_distance(10, 'kilometers', 'miles')
    print(result3)