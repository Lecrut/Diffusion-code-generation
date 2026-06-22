def convert_distance(value, source_unit):
    conversion_factors = {'m': 1.0, 'km': 1000.0, 'mi': 1609.344, 'ft': 0.3048}
    if not isinstance(value, (int, float)):
        raise ValueError('Value must be a numeric type.')
    if source_unit not in conversion_factors:
        raise ValueError("Unsupported source unit. Use 'm', 'km', 'mi', or 'ft'.")
    meters = value * conversion_factors[source_unit]
    return round(meters, 6)
if __name__ == '__main__':
    print(convert_distance(10, 'm'))
    print(convert_distance(5, 'km'))
    print(convert_distance(2, 'mi'))
    print(convert_distance(100, 'ft'))