GALLON_TO_LITER = 3.78541
LITER_TO_GALLON = 1 / GALLON_TO_LITER

def convert(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == 'gal':
        if to_unit == 'l':
            return round(value * GALLON_TO_LITER, 2)
        else:
            raise ValueError("Invalid conversion to unit")
    elif from_unit == 'l':
        if to_unit == 'gal':
            return round(value * LITER_TO_GALLON, 2)
        else:
            raise ValueError("Invalid conversion to unit")
    else:
        raise ValueError("Invalid source unit provided")

if __name__ == '__main__':
    print(f"10 gal to l: {convert(10.0, 'gal', 'l')}")
    print(f"5 l to gal: {convert(5.0, 'l', 'gal')}")
    print(f"20 gal to l: {convert(20.0, 'gal', 'l')}")