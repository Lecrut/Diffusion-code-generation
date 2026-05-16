import math
def volume_to_liters(volume: float, unit: str) -> float:
    if unit == "L":
        return volume
    elif unit == "m^3":
        return volume * 1000.0
    elif unit == "mL":
        return volume / 1000.0
    elif unit == "cm^3":
        return volume * 1e-6
    elif unit == "in^3":
        return volume * 16.387064e-6
    elif unit == "ft^3":
        return volume * 28.316846592
    elif unit == "gal":
        return volume * 3.785411784
    elif unit == "qt":
        return volume * 0.946352946
    elif unit == "fl_oz":
        return volume * 0.0295735295625
    else:
        raise ValueError(f"Unsupported unit: {unit}")
if __name__ == '__main__':
    test_cases = [
        (1.0, "L"),
        (1.0, "m^3"),
        (1000.0, "mL"),
        (1000000.0, "cm^3"),
        (1.0, "in^3"),
        (1.0, "ft^3"),
        (1.0, "gal"),
        (1.0, "qt"),
        (1.0, "fl_oz")
    ]
    for volume, unit in test_cases:
        try:
            result = volume_to_liters(volume, unit)
            print(f"Volume: {volume} {unit} -> Liters: {result}")
        except ValueError as e:
            print(f"Error processing {volume} {unit}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {volume} {unit}: {e}")