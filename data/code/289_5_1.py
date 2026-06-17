def convert_distance(value, from_unit, to_unit):
    conversions = {
        'km': 1000.0,
        'mi': 1609.34,
        'm': 1.0,
        'ft': 0.3048
    }
    if from_unit == to_unit:
        return value
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError("Invalid unit specified")
    base = 'm'
    if from_unit == 'km':
        value_in_base = value * 1000.0
    elif from_unit == 'mi':
        value_in_base = value * 1609.34
    elif from_unit == 'm':
        value_in_base = value
    elif from_unit == 'ft':
        value_in_base = value * 0.3048
    else:
        raise ValueError("Unknown source unit")
    if to_unit == 'km':
        return value_in_base / 1000.0
    elif to_unit == 'mi':
        return value_in_base / 1609.34
    elif to_unit == 'm':
        return value_in_base
    elif to_unit == 'ft':
        return value_in_base / 0.3048
    else:
        raise ValueError("Unknown target unit")
if __name__ == '__main__':
    print(f"10 km to mi: {convert_distance(10, 'km', 'mi'):.2f}")
    print(f"10 mi to km: {convert_distance(10, 'mi', 'km'):.2f}")
    print(f"5000 m to ft: {convert_distance(5000, 'm', 'ft'):.2f}")
    print(f"100 ft to m: {convert_distance(100, 'ft', 'm'):.2f}")
    print(f"1 mile to km: {convert_distance(1, 'mi', 'km'):.2f}")
    print(f"1000 m to km: {convert_distance(1000, 'm', 'km'):.2f}")