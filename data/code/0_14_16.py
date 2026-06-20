def convert_length(value, from_unit, to_unit):
    factors = {
        'meters': 1.0,
        'kilometers': 0.001,
        'centimeters': 100.0,
        'millimeters': 1000.0,
        'inches': 39.3701,
        'feet': 3.28084,
        'yards': 1.09361,
        'miles': 0.000621371
    }
    if from_unit not in factors or to_unit not in factors:
        raise ValueError("Invalid unit")
    in_meters = value / factors[from_unit]
    return in_meters * factors[to_unit]

if __name__ == '__main__':
    result1 = convert_length(1, 'kilometers', 'meters')
    print(result1)
    result2 = convert_length(100, 'centimeters', 'inches')
    print(result2)
    result3 = convert_length(1, 'miles', 'feet')
    print(result3)