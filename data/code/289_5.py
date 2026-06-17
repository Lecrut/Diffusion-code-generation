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
    base_value = value * conversions[from_unit] / conversions[to_unit]
    return base_value
if __name__ == '__main__':
    print(f"10 km to mi: {convert_distance(10, 'km', 'mi'):.2f}")
    print(f"5 mi to km: {convert_distance(5, 'mi', 'km'):.2f}")
    print(f"1000 m to ft: {convert_distance(1000, 'm', 'ft'):.2f}")
    print(f"10 ft to m: {convert_distance(10, 'ft', 'm'):.2f}")
    print(f"1 mi to km: {convert_distance(1, 'mi', 'km'):.2f}")
    print(f"500000 m to km: {convert_distance(500000, 'm', 'km'):.2f}")