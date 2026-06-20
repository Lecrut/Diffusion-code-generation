def convert_distance(value, from_unit, to_unit):
    if value < 0:
        raise ValueError("Distance cannot be negative")
    if from_unit not in ('meters', 'kilometers', 'miles'):
        raise ValueError("Invalid from_unit")
    if to_unit not in ('meters', 'kilometers', 'miles'):
        raise ValueError("Invalid to_unit")

    conversion_to_meters = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'miles': 1609.344
    }

    meters = value * conversion_to_meters[from_unit]
    result = meters / conversion_to_meters[to_unit]

    return result

if __name__ == '__main__':
    sample_values = [
        (1000, 'meters', 'kilometers'),
        (1, 'kilometers', 'meters'),
        (1, 'miles', 'kilometers'),
        (5, 'kilometers', 'miles'),
        (1609.344, 'meters', 'miles')
    ]

    for val, from_u, to_u in sample_values:
        converted = convert_distance(val, from_u, to_u)
        print(f"{val} {from_u} = {converted} {to_u}")