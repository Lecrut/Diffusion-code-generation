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
    raise ValueError("Invalid unit specified.")
if __name__ == '__main__':
    distance_m = 5000.0
    from_unit = 'm'
    to_unit = 'km'
    try:
        result = convert_distance(distance_m, from_unit, to_unit)
        print(f"{distance_m} meters is equal to {result:.4f} kilometers")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    distance_km = 10.0
    from_unit = 'km'
    to_unit = 'mi'
    try:
        result = convert_distance(distance_km, from_unit, to_unit)
        print(f"{distance_km} kilometers is equal to {result:.4f} miles")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    distance_mi = 1000.0
    from_unit = 'mi'
    to_unit = 'm'
    try:
        result = convert_distance(distance_mi, from_unit, to_unit)
        print(f"{distance_mi} miles is equal to {result:.4f} meters")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    distance_m_to_m = 100.0
    from_unit = 'm'
    to_unit = 'm'
    try:
        result = convert_distance(distance_m_to_m, from_unit, to_unit)
        print(f"{distance_m_to_m} meters is equal to {result:.4f} meters")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    distance_invalid = 10.0
    from_unit = 'm'
    to_unit = 'lightyears'
    try:
        result = convert_distance(distance_invalid, from_unit, to_unit)
        print(f"{distance_invalid} meters is equal to {result:.4f} lightyears")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)