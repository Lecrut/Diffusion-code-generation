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
        raise ValueError("Unknown unit provided.")
    if from_unit == "L":
        value_in_liters = value
    elif from_unit == "mL":
        value_in_liters = value / 1000.0
    elif from_unit == "m^3":
        value_in_liters = value * 1000.0
    elif from_unit == "gal":
        value_in_liters = value * 3.78541
    else:
        raise ValueError("Unsupported input unit.")
    if to_unit == "L":
        result = value_in_liters
    elif to_unit == "mL":
        result = value_in_liters * 1000.0
    elif to_unit == "m^3":
        result = value_in_liters / 1000000.0
    elif to_unit == "gal":
        result = value_in_liters / 3.78541
    else:
        raise ValueError("Unsupported output unit.")
    return result
def main():
    sample_value = 5.5
    from_unit = "L"
    to_unit = "gal"
    print(f"Sample Value: {sample_value} {from_unit}")
    try:
        converted_value = convert_volume(sample_value, from_unit, to_unit)
        print(f"Converted Value: {converted_value:.4f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 20)
    sample_value_2 = 1000
    from_unit_2 = "mL"
    to_unit_2 = "m^3"
    print(f"Sample Value: {sample_value_2} {from_unit_2}")
    try:
        converted_value_2 = convert_volume(sample_value_2, from_unit_2, to_unit_2)
        print(f"Converted Value: {converted_value_2:.6f} {to_unit_2}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == '__main__':
    main()