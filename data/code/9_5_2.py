import math
def volume_to_liters(volume: float, unit: str) -> float:
    if unit.lower() == "liter":
        return volume
    elif unit.lower() == "l":
        return volume
    elif unit.lower() == "ml":
        return volume / 1000.0
    elif unit.lower() == "milliliter":
        return volume / 1000.0
    elif unit.lower() == "cm3":
        return volume / 1000000.0
    elif unit.lower() == "cc":
        return volume / 1000.0
    elif unit.lower() == "m3":
        return volume * 1000.0
    elif unit.lower() == "cubic meter":
        return volume * 1000.0
    elif unit.lower() == "cubic meter":
        return volume * 1000.0
    else:
        raise ValueError(f"Unsupported unit: {unit}")
if __name__ == '__main__':
    test_cases = [
        (1.0, "liter"),
        (2.5, "L"),
        (500.0, "ml"),
        (1000.0, "cc"),
        (0.001, "cm3"),
        (1.0, "cubic meter"),
        (10.0, "m3"),
        (123.456789, "liter"),
        (987654321.0, "milliliter")
    ]
    for volume, unit in test_cases:
        try:
            result = volume_to_liters(volume, unit)
            print(f"Volume: {volume} {unit} -> Liters: {result}")
        except ValueError as e:
            print(f"Error for Volume: {volume} {unit}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for Volume: {volume} {unit}: {e}")
    print("-" * 20)
    try:
        volume_to_liters(10.0, "gallon")
    except ValueError as e:
        print(f"Test unsupported unit: {e}")