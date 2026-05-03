import math
def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        "L": 1.0,
        "mL": 1000.0,
        "m^3": 1000000.0,
        "gal": 3.78541,
    }
    if from_unit == to_unit:
        return value
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit specified.")
    if from_unit == "L":
        value_in_liters = value
    elif from_unit == "mL":
        value_in_liters = value / 1000.0
    elif from_unit == "m^3":
        value_in_liters = value * 1000000.0
    elif from_unit == "gal":
        value_in_liters = value * 3.78541
    if to_unit == "L":
        return value_in_liters
    elif to_unit == "mL":
        return value_in_liters * 1000.0
    elif to_unit == "m^3":
        return value_in_liters / 1000000.0
    elif to_unit == "gal":
        return value_in_liters / 3.78541
    else:
        raise ValueError("Target unit not supported.")
if __name__ == '__main__':
    sample_value = 5.5
    from_unit = "L"
    to_unit = "mL"
    result = convert_volume(sample_value, from_unit, to_unit)
    print(f"Sample Value: {sample_value} {from_unit}")
    print(f"Converted Value: {result} {to_unit}")
    sample_value_2 = 1.5
    from_unit_2 = "m^3"
    to_unit_2 = "gal"
    result_2 = convert_volume(sample_value_2, from_unit_2, to_unit_2)
    print(f"\nSample Value: {sample_value_2} {from_unit_2}")
    print(f"Converted Value: {result_2} {to_unit_2}")