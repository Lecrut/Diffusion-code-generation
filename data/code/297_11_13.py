def validate_unit(unit: str) -> bool:
    return unit in {"gal", "l"}

def convert_gallons_to_liters(gallons: float) -> float:
    conversion_factor = 3.78541
    return round(gallons * conversion_factor, 2)

def convert_liters_to_gallons(liters: float) -> float:
    conversion_factor = 1 / 3.78541
    return round(liters * conversion_factor, 2)

def convert(value: float, from_unit: str, to_unit: str) -> float:
    if not validate_unit(from_unit) or not validate_unit(to_unit):
        raise ValueError("Invalid unit provided")
    if from_unit == "gal":
        if to_unit == "l":
            return convert_gallons_to_liters(value)
        else:
            raise ValueError("Unsupported conversion")
    elif from_unit == "l":
        if to_unit == "gal":
            return convert_liters_to_gallons(value)
        else:
            raise ValueError("Unsupported conversion")
    else:
        raise ValueError("Invalid unit provided")

if __name__ == '__main__':
    print(f"10 gal to l: {convert(10.0, 'gal', 'l')}")
    print(f"5 l to gal: {convert(5.0, 'l', 'gal')}")