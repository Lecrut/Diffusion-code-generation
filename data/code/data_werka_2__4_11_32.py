def convert_distance(value, source_unit):
    M_TO_KM = 1 / 1000.0
    M_TO_MI = 1 / 1609.344
    M_TO_FT = 3.28084
    if not isinstance(value, (int, float)):
        raise ValueError('Value must be a numeric type.')
    conversion_factors = {'meters': 1.0, 'kilometers': M_TO_KM, 'miles': M_TO_MI, 'feet': M_TO_FT}
    if source_unit not in conversion_factors:
        raise ValueError(f'Unsupported unit: {source_unit}')
    meters = value * conversion_factors[source_unit]

    def to_meters(val):
        return val / conversion_factors['meters']
    converted_values = {'meters': round(meters, 6), 'kilometers': round(to_meters(meters), 6), 'miles': round(to_meters(meters) * M_TO_MI, 6), 'feet': round(to_meters(meters) * M_TO_FT, 6)}
    return converted_values[source_unit]
if __name__ == '__main__':
    print(convert_distance(100, 'meters'))
    print(convert_distance(100, 'kilometers'))
    print(convert_distance(100, 'miles'))
    print(convert_distance(100, 'feet'))