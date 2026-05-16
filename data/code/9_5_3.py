import math
def convert_to_liters(volume: float, unit: str) -> float:
    if unit.lower() == "liter":
        return volume
    elif unit.lower() == "l":
        return volume
    elif unit.lower() == "milliliter":
        return volume / 1000.0
    elif unit.lower() == "ml":
        return volume / 1000.0
    elif unit.lower() == "cubic meter":
        return volume * 1000.0
    elif unit.lower() == "m3":
        return volume * 1000.0
    elif unit.lower() == "cubic foot":
        return volume * 28.316846592
    elif unit.lower() == "ft3":
        return volume * 28.316846592
    elif unit.lower() == "gallon":
        return volume * 3.785411784
    elif unit.lower() == "us_gallon":
        return volume * 3.785411784
    elif unit.lower() == "pint":
        return volume * 0.473176473
    elif unit.lower() == "fluid_ounce":
        return volume * 0.0295735295625
    else:
        raise ValueError(f"Unsupported unit: {unit}")
if __name__ == '__main__':
    test_cases = [
        (1.0, "liter"),
        (2.5, "gallon"),
        (1000.0, "milliliter"),
        (0.5, "cubic meter"),
        (10.0, "cubic foot"),
        (100.0, "us_gallon"),
        (1.0, "pint"),
        (100.0, "fluid_ounce"),
        (5.0, "unknown_unit")
    ]
    for volume, unit in test_cases:
        try:
            result = convert_to_liters(volume, unit)
            print(f"Volume: {volume} {unit} -> Liters: {result}")
        except ValueError as e:
            print(f"Error for Volume: {volume} {unit}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for Volume: {volume} {unit}: {e}")
        print("-" * 20)