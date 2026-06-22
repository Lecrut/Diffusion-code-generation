def validate_value(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a numeric type.")

def validate_unit(source_unit):
    supported_units = ['meters', 'kilometers', 'miles', 'feet']
    if source_unit not in supported_units:
        raise ValueError(f"Unsupported unit: {source_unit}")

def convert_to_meters(value, source_unit):
    conversion_factors = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'miles': 1609.344,
        'feet': 0.3048
    }
    return value * conversion_factors[source_unit]

def convert_distance(value, source_unit):
    validate_value(value)
    validate_unit(source_unit)
    meters = convert_to_meters(value, source_unit)
    converted_values = {
        'meters': round(meters, 6),
        'kilometers': round(meters / 1000.0, 6),
        'miles': round(meters / 1609.344, 6),
        'feet': round(meters / 0.3048, 6)
    }
    return converted_values[source_unit]

if __name__ == '__main__':
    print(convert_distance(100, 'meters'))
    print(convert_distance(50, 'kilometers'))
    print(convert_distance(20, 'miles'))
    print(convert_distance(3000, 'feet'))