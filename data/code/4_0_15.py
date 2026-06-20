def convert_distance(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    meters = value
    if from_unit == 'kilometers':
        meters = value * 1000
    elif from_unit == 'miles':
        meters = value * 1609.344
    elif from_unit == 'meters':
        meters = value
    else:
        raise ValueError(f"Unknown source unit: {from_unit}")
    result = meters
    if to_unit == 'kilometers':
        result = meters / 1000
    elif to_unit == 'miles':
        result = meters / 1609.344
    elif to_unit == 'meters':
        result = meters
    else:
        raise ValueError(f"Unknown target unit: {to_unit}")
    return result

if __name__ == '__main__':
    sample_values = [
        (1000, 'meters', 'kilometers'),
        (5, 'kilometers', 'miles'),
        (1, 'miles', 'meters'),
        (0, 'meters', 'kilometers'),
        (-5, 'kilometers', 'miles'),
    ]
    for val, frm, to in sample_values:
        result = convert_distance(val, frm, to)
        print(f"{val} {frm} = {result} {to}")