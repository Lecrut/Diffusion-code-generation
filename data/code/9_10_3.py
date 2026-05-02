import math
def convert_volume(value, unit, target_unit):
    conversion_factors = {
        "L": 1.0,
        "mL": 0.001,
        "m^3": 1000.0,
        "gal": 3.78541
    }
    if unit == target_unit:
        return value
    if unit == "L" or unit == "mL":
        base_value = value
        if unit == "L":
            base_value = value
        elif unit == "mL":
            base_value = value * 0.001
        if target_unit == "L":
            return base_value
        elif target_unit == "mL":
            return base_value * 1000.0
        elif target_unit == "m^3":
            return base_value / 1000.0
        elif target_unit == "gal":
            return base_value / 3.78541
    if unit == "m^3" or unit == "L":
        base_value = value
        if unit == "m^3":
            base_value = value * 1000.0
        elif unit == "L":
            base_value = value
        if target_unit == "m^3":
            return base_value / 1000.0
        elif target_unit == "L":
            return base_value
        elif target_unit == "mL":
            return base_value * 1000.0
        elif target_unit == "gal":
            return base_value / 3.78541
    if unit == "gal":
        base_value = value
        if target_unit == "L":
            return base_value * 3.78541
        elif target_unit == "mL":
            return base_value * 3.78541 * 1000.0
        elif target_unit == "m^3":
            return base_value * (1 / 3.78541) * (1 / 1000.0)
        elif target_unit == "gal":
            return base_value
    return None
def main():
    sample_value = 5.5
    sample_unit = "L"
    target_unit = "gal"
    print(f"Original Value: {sample_value} {sample_unit}")
    result = convert_volume(sample_value, sample_unit, target_unit)
    if result is not None:
        print(f"Converted Value: {result:.4f} {target_unit}")
    else:
        print("Conversion failed.")
if __name__ == '__main__':
    main()