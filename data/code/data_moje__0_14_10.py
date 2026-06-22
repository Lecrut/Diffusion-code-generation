import math

def convert_length(value, from_unit, to_unit):
    meters = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }

    if from_unit not in meters:
        raise ValueError(f"Unknown unit: {from_unit}")
    if to_unit not in meters:
        raise ValueError(f"Unknown unit: {to_unit}")

    value_in_meters = value * meters[from_unit]
    result = value_in_meters / meters[to_unit]
    return result

if __name__ == '__main__':
    val = convert_length(1, 'km', 'mi')
    print(val)

    val2 = convert_length(12, 'in', 'cm')
    print(val2)

    val3 = convert_length(5280, 'ft', 'mi')
    print(val3)