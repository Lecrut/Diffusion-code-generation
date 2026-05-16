import math
def convert_volume(value, unit):
    conversion_factors = {
        "L": 1.0,
        "mL": 1000.0,
        "m3": 1000.0,
        "gal": 3.78541
    }
    if unit not in conversion_factors:
        raise ValueError(f"Unknown unit: {unit}")
    if unit == "L":
        base_value = value
    elif unit == "mL":
        base_value = value / 1000.0
    elif unit == "m3":
        base_value = value * 1000.0
    elif unit == "gal":
        base_value = value / 3.78541
    else:
        raise ValueError("Invalid unit specified.")
    if unit == "L":
        return base_value
    elif unit == "mL":
        return base_value * 1000.0
    elif unit == "m3":
        return base_value / 1000.0
    elif unit == "gal":
        return base_value * 3.78541
    else:
        raise ValueError("Conversion logic error.")
if __name__ == '__main__':
    sample_value = 5.0
    sample_unit = "L"
    print(f"Original Value: {sample_value} {sample_unit}")
    try:
        result = convert_volume(sample_value, sample_unit)
        print(f"Converted Value: {result}")
        print("\n--- Sample Conversions ---")
        value_liters = 10.0
        print(f"{value_liters} L is equal to: {convert_volume(value_liters, 'mL'):.2f} mL")
        value_m3 = 2.5
        print(f"{value_m3} m3 is equal to: {convert_volume(value_m3, 'L'):.2f} L")
        value_gal = 10.0
        print(f"{value_gal} gal is equal to: {convert_volume(value_gal, 'L'):.2f} L")
    except ValueError as e:
        print(f"Error: {e}")