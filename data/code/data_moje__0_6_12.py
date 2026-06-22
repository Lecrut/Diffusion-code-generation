def convert_length(value, from_unit, to_unit):
    units = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344,
        'nmi': 1852.0
    }
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    if from_unit_lower not in units:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit_lower not in units:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    meters = value * units[from_unit_lower]
    return meters / units[to_unit_lower]

if __name__ == '__main__':
    result_m_to_ft = convert_length(100, 'm', 'ft')
    result_km_to_mi = convert_length(5, 'km', 'mi')
    result_in_to_cm = convert_length(12, 'in', 'cm')
    result_mi_to_m = convert_length(1, 'mi', 'm')
    print(result_m_to_ft)
    print(result_km_to_mi)
    print(result_in_to_cm)
    print(result_mi_to_m)