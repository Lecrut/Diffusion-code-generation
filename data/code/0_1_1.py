def convert_length(length: float, unit: str) -> float:
    conversion_factors = {
        'm': 1.0,
        'ft': 0.3048,
        'in': 0.0254,
        'km': 1000.0,
        'mi': 1609.34
    }
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit type: {unit}")
    if unit == 'm':
        return length
    elif unit == 'ft':
        return length * 0.3048
    elif unit == 'in':
        return length * 0.0254
    elif unit == 'km':
        return length * 1000.0
    elif unit == 'mi':
        return length * 1609.34
    else:
        return length
if __name__ == '__main__':
    length_m = 10.0
    unit_m = 'm'
    result_m = convert_length(length_m, unit_m)
    print(f"Converting {length_m} {unit_m} to other units: {result_m}")
    length_ft = 10.0
    unit_ft = 'ft'
    result_ft = convert_length(length_ft, unit_ft)
    print(f"Converting {length_ft} {unit_ft} to meters: {result_ft}")
    length_in = 12.0
    unit_in = 'in'
    result_in = convert_length(length_in, unit_in)
    print(f"Converting {length_in} {unit_in} to meters: {result_in}")
    length_km = 5.0
    unit_km = 'km'
    result_km = convert_length(length_km, unit_km)
    print(f"Converting {length_km} {unit_km} to meters: {result_km}")
    length_mi = 1.0
    unit_mi = 'mi'
    result_mi = convert_length(length_mi, unit_mi)
    print(f"Converting {length_mi} {unit_mi} to meters: {result_mi}")