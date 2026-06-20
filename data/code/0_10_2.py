def _to_meters(length, unit):
    conversion_factors = {
        "meters": 1.0,
        "feet": 0.3048,
        "kilometers": 1000.0
    }
    normalized_unit = unit.lower()
    if normalized_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    return length * conversion_factors[normalized_unit]

def _from_meters(length_meters, target_unit):
    conversion_rates = {
        "meters": 1.0,
        "feet": 1.0 / 0.3048,
        "kilometers": 0.001
    }
    normalized_target = target_unit.lower()
    if normalized_target not in conversion_rates:
        raise ValueError(f"Unsupported unit: {target_unit}")
    return length_meters * conversion_rates[normalized_target]

def convert_length(length, target_unit):
    base_meters = _to_meters(length, target_unit)
    return _from_meters(base_meters, target_unit)

def convert_length_to_unit(length, input_unit, target_unit):
    base_meters = _to_meters(length, input_unit)
    return _from_meters(base_meters, target_unit)

if __name__ == '__main__':
    val1 = convert_length_to_unit(10, "feet", "meters")
    print(val1)
    val2 = convert_length_to_unit(1, "kilometers", "feet")
    print(val2)
    val3 = convert_length_to_unit(1000, "meters", "kilometers")
    print(val3)
    try:
        convert_length_to_unit(50, "inches", "feet")
    except ValueError as error:
        print(error)