def convert_length(length: float, unit: str) -> float:
    conversion_factors = {
        'm': 1.0,
        'ft': 0.3048,
        'in': 0.0254,
        'km': 1000.0,
        'mi': 1609.34
    }
    if unit in conversion_factors:
        return length * conversion_factors[unit]
    else:
        raise ValueError(f"Unsupported unit type: {unit}")
if __name__ == '__main__':
    length_m = 10.0
    unit_m = 'm'
    result_m = convert_length(length_m, unit_m)
    print(f"{length_m} {unit_m} is {result_m}")
    length_ft = 5.0
    unit_ft = 'ft'
    result_ft = convert_length(length_ft, unit_ft)
    print(f"{length_ft} {unit_ft} is {result_ft}")
    length_in = 100.0
    unit_in = 'in'
    result_in = convert_length(length_in, unit_in)
    print(f"{length_in} {unit_in} is {result_in}")
    length_km = 2.5
    unit_km = 'km'
    result_km = convert_length(length_km, unit_km)
    print(f"{length_km} {unit_km} is {result_km}")
    try:
        convert_length(10.0, 'lightyear')
    except ValueError as e:
        print(f"Error caught: {e}")