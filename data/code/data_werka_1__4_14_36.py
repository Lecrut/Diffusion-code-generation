def convert_distance(value, source_unit):
    conversion_factors = {'meters': {'meters': 1.0, 'kilometers': 0.001, 'miles': 0.000621371, 'feet': 3.28084}, 'kilometers': {'meters': 1000.0, 'kilometers': 1.0, 'miles': 0.621371, 'feet': 3280.84}, 'miles': {'meters': 1609.34, 'kilometers': 1.60934, 'miles': 1.0, 'feet': 5280.0}, 'feet': {'meters': 0.3048, 'kilometers': 0.0003048, 'miles': 0.000189394, 'feet': 1.0}}
    if not isinstance(value, (int, float)):
        raise ValueError('Value must be a numeric type.')
    if source_unit not in conversion_factors:
        raise ValueError("Invalid source unit. Choose from 'meters', 'kilometers', 'miles', or 'feet'.")
    return round(value * conversion_factors[source_unit][source_unit], 6)
if __name__ == '__main__':
    print(convert_distance(100, 'meters'))
    print(convert_distance(5, 'kilometers'))
    print(convert_distance(2, 'miles'))
    print(convert_distance(3048, 'feet'))