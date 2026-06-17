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
    base_value = value
    if from_unit == 'km':
        base_value = value * 1000.0
    elif from_unit == 'mi':
        base_value = value * 1609.34
    elif from_unit == 'm':
        base_value = value * 1.0
    elif from_unit == 'ft':
        base_value = value * 0.3048
    if to_unit == 'km':
        return base_value / 1000.0
    elif to_unit == 'mi':
        return base_value / 1609.34
    elif to_unit == 'm':
        return base_value / 1.0
    elif to_unit == 'ft':
        return base_value / 0.3048
    else:
        raise ValueError("Invalid target unit specified")
if __name__ == '__main__':
    print(f"10 km to mi: {convert_distance(10, 'km', 'mi'):.2f}")
    print(f"10 mi to km: {convert_distance(10, 'mi', 'km'):.2f}")
    print(f"5000 m to ft: {convert_distance(5000, 'm', 'ft'):.2f}")
    print(f"10000 ft to km: {convert_distance(10000, 'ft', 'km'):.2f}")
    print(f"1 mi to m: {convert_distance(1, 'mi', 'm'):.2f}")
    print(f"50 ft to mi: {convert_distance(50, 'ft', 'mi'):.2f}")