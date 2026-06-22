UNIT_CONVERSIONS = {
    'm': {'mm': 1000, 'cm': 100, 'dm': 10, 'dam': 0.1, 'hm': 0.01, 'km': 0.001,
          'in': 39.3701, 'ft': 3.28084, 'yd': 1.09361, 'mi': 0.000621371},
    'mm': {'m': 0.001, 'cm': 0.1, 'dm': 0.01, 'dam': 0.0001, 'hm': 0.00001, 'km': 0.000001,
           'in': 0.0393701, 'ft': 0.00328084, 'yd': 0.00109361, 'mi': 0.000000621371},
    'cm': {'m': 0.01, 'mm': 10, 'dm': 0.1, 'dam': 0.001, 'hm': 0.0001, 'km': 0.00001,
           'in': 0.393701, 'ft': 0.0328084, 'yd': 0.0109361, 'mi': 0.00000621371},
    'dm': {'m': 0.1, 'mm': 100, 'cm': 10, 'dam': 0.01, 'hm': 0.001, 'km': 0.0001,
           'in': 3.93701, 'ft': 0.328084, 'yd': 0.109361, 'mi': 0.00000621371},
    'dam': {'m': 10, 'mm': 10000, 'cm': 1000, 'dm': 100, 'hm': 0.1, 'km': 0.01,
            'in': 393.701, 'ft': 32.8084, 'yd': 10.9361, 'mi': 0.00621371},
    'hm': {'m': 100, 'mm': 100000, 'cm': 10000, 'dm': 1000, 'dam': 10, 'km': 0.1,
           'in': 3937.01, 'ft': 328.084, 'yd': 109.361, 'mi': 0.0621371},
    'km': {'m': 1000, 'mm': 1000000, 'cm': 100000, 'dm': 10000, 'dam': 100, 'hm': 10,
           'in': 39370.1, 'ft': 3280.84, 'yd': 1093.61, 'mi': 0.621371},
    'in': {'m': 0.0254, 'mm': 25.4, 'cm': 2.54, 'dm': 0.254, 'dam': 0.00254, 'hm': 0.000254, 'km': 0.0000254,
           'ft': 0.0833333, 'yd': 0.0277778, 'mi': 0.0000157828},
    'ft': {'m': 0.3048, 'mm': 304.8, 'cm': 30.48, 'dm': 3.048, 'dam': 0.03048, 'hm': 0.003048, 'km': 0.0003048,
           'in': 12, 'yd': 0.333333, 'mi': 0.000189394},
    'yd': {'m': 0.9144, 'mm': 914.4, 'cm': 91.44, 'dm': 9.144, 'dam': 0.09144, 'hm': 0.009144, 'km': 0.0009144,
           'in': 36, 'ft': 3, 'mi': 0.000568182},
    'mi': {'m': 1609.34, 'mm': 1609340, 'cm': 160934, 'dm': 16093.4, 'dam': 160.934, 'hm': 16.0934, 'km': 1.60934,
           'in': 63360, 'ft': 5280, 'yd': 1760}
}

def convert_length(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in UNIT_CONVERSIONS:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in UNIT_CONVERSIONS[from_unit]:
        raise ValueError(f"Cannot convert from {from_unit} to {to_unit}")
    factor = UNIT_CONVERSIONS[from_unit][to_unit]
    return value * factor

if __name__ == '__main__':
    result1 = convert_length(1, 'km', 'mi')
    print(result1)
    result2 = convert_length(5, 'ft', 'm')
    print(result2)
    result3 = convert_length(100, 'cm', 'in')
    print(result3)
    result4 = convert_length(1, 'm', 'm')
    print(result4)
    result5 = convert_length(2.5, 'mi', 'km')
    print(result5)