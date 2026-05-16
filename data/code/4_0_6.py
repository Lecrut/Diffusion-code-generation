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
    raise ValueError("Invalid unit specified. Must be 'm', 'km', or 'mi'.")
if __name__ == '__main__':
    distance_m = 5000.0
    from_unit = 'm'
    to_unit = 'km'
    distance_mi = 10.0
    from_unit = 'mi'
    to_unit = 'm'
    distance_km = 100.0
    from_unit = 'km'
    to_unit = 'mi'
    print(f"{distance_m} {from_unit} to {to_unit}: {convert_distance(distance_m, from_unit, to_unit):.4f}")
    print(f"{distance_mi} {from_unit} to {to_unit}: {convert_distance(distance_mi, from_unit, to_unit):.4f}")
    print(f"{distance_km} {from_unit} to {to_unit}: {convert_distance(distance_km, from_unit, to_unit):.4f}")
    try:
        convert_distance(100, 'm', 'lightyear')
    except ValueError as e:
        print(f"Error caught: {e}")