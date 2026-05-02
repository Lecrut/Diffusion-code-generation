import sys
def convert_distance(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'm':
        if to_unit == 'km':
            return value / 1000.0
        elif to_unit == 'mi':
            return value / 1609.34
    elif from_unit == 'km':
        if to_unit == 'm':
            return value * 1000.0
        elif to_unit == 'mi':
            return value / 1.60934
    elif from_unit == 'mi':
        if to_unit == 'km':
            return value * 1.60934
        elif to_unit == 'm':
            return value * 1609.34
    raise ValueError("Invalid unit combination or unsupported conversion.")
if __name__ == '__main__':
    distance_m = 5000
    from_unit = 'm'
    to_unit = 'km'
    print(f"Original value: {distance_m} {from_unit}")
    try:
        result = convert_distance(distance_m, from_unit, to_unit)
        print(f"Converted value: {result:.4f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    distance_km = 10
    from_unit = 'km'
    to_unit = 'mi'
    print(f"\nOriginal value: {distance_km} {from_unit}")
    try:
        result = convert_distance(distance_km, from_unit, to_unit)
        print(f"Converted value: {result:.4f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    distance_mi = 100
    from_unit = 'mi'
    to_unit = 'm'
    print(f"\nOriginal value: {distance_mi} {from_unit}")
    try:
        result = convert_distance(distance_mi, from_unit, to_unit)
        print(f"Converted value: {result:.4f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    distance_m_to_m = 100
    from_unit = 'm'
    to_unit = 'm'
    print(f"\nOriginal value: {distance_m_to_m} {from_unit}")
    try:
        result = convert_distance(distance_m_to_m, from_unit, to_unit)
        print(f"Converted value: {result:.4f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    distance_invalid = 10
    from_unit = 'm'
    to_unit = 'lightyears'
    print(f"\nOriginal value: {distance_invalid} {from_unit}")
    try:
        result = convert_distance(distance_invalid, from_unit, to_unit)
        print(f"Converted value: {result:.4f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)