def convert_distance(value, from_unit, to_unit):
    if value < 0:
        raise ValueError("Distance cannot be negative")
    valid_units = {'meters', 'kilometers', 'miles'}
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError("Invalid unit. Use 'meters', 'kilometers', or 'miles'.")
    conversion_factors = {
        'meters': {'meters': 1, 'kilometers': 0.001, 'miles': 0.000621371},
        'kilometers': {'meters': 1000, 'kilometers': 1, 'miles': 0.621371},
        'miles': {'meters': 1609.34, 'kilometers': 1.60934, 'miles': 1}
    }
    factor = conversion_factors[from_unit][to_unit]
    return value * factor

if __name__ == '__main__':
    samples = [
        (1000, 'meters', 'kilometers'),
        (1, 'kilometers', 'miles'),
        (5, 'miles', 'meters'),
        (1500, 'meters', 'miles'),
        (2.5, 'kilometers', 'meters')
    ]
    for value, from_u, to_u in samples:
        result = convert_distance(value, from_u, to_u)
        print(f"{value} {from_u} = {result} {to_u}")