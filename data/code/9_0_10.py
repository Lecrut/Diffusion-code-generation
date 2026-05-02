import math
def convert_volume(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "L":
        if to_unit == "mL":
            return value * 1000
        elif to_unit == "m^3":
            return value / 1000
        elif to_unit == "gal":
            return value * 0.264172
        elif to_unit == "in^3":
            return value * 610.237
    elif from_unit == "mL":
        if to_unit == "L":
            return value / 1000
        elif to_unit == "m^3":
            return value / 1000000
        elif to_unit == "gal":
            return value * 0.00378541
        elif to_unit == "in^3":
            return value * 0.0000610237
    elif from_unit == "m^3":
        if to_unit == "L":
            return value * 1000
        elif to_unit == "mL":
            return value * 1000000
        elif to_unit == "gal":
            return value / 0.00378541
        elif to_unit == "in^3":
            return value * 16387.064
    elif from_unit == "gal":
        if to_unit == "L":
            return value * 3.78541
        elif to_unit == "mL":
            return value * 3785.41
        elif to_unit == "m^3":
            return value * 0.00378541
        elif to_unit == "in^3":
            return value * 16387.064
    elif from_unit == "in^3":
        if to_unit == "L":
            return value * 0.0000264172
        elif to_unit == "mL":
            return value * 0.0000610237
        elif to_unit == "m^3":
            return value * 1.6387064e-5
        elif to_unit == "gal":
            return value / 16387.064
    else:
        return "Error: Unknown unit"
def main():
    sample_value = 10
    from_unit = "L"
    to_unit = "gal"
    print(f"Sample Value: {sample_value} {from_unit}")
    conversions = [
        ("L", "mL", 1000),
        ("L", "m^3", 0.001),
        ("L", "gal", 0.264172),
        ("L", "in^3", 610.237),
        ("mL", "L", 0.001),
        ("mL", "m^3", 1e-6),
        ("mL", "gal", 0.00378541),
        ("mL", "in^3", 0.0000610237),
        ("m^3", "L", 1000),
        ("m^3", "mL", 1e6),
        ("m^3", "gal", 2641.72),
        ("m^3", "in^3", 16387.064),
        ("gal", "L", 3.78541),
        ("gal", "mL", 3785.41),
        ("gal", "m^3", 0.00378541),
        ("gal", "in^3", 16387.064),
        ("in^3", "L", 0.0000264172),
        ("in^3", "mL", 0.0000610237),
        ("in^3", "m^3", 1.6387064e-5),
        ("in^3", "gal", 1/16387.064)
    ]
    for from_unit_s, to_unit_s, factor in conversions:
        result = convert_volume(sample_value, from_unit_s, to_unit_s)
        print(f"{sample_value} {from_unit_s} is equal to {result:.6f} {to_unit_s}")
if __name__ == '__main__':
    main()