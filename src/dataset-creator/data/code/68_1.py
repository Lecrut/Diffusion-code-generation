def convert_to_liters(volume_str: str) -> float:
    volume = float(volume_str.strip())
    unit_map = {
        'ml': 0.001,
        'liter': 1.0,
        'liters': 1.0,
        'l': 1.0,
        'cl': 0.01,
        'dL': 0.1,
        'm3': 1000.0,
    }
    unit = volume_str.lower().split()[1] if ' ' in volume_str else ''
    for key, value in unit_map.items():
        if unit == key:
            return volume * value
    raise ValueError(f"Unsupported unit: {unit}")
if __name__ == '__main__':
    test_cases = [
        "50 ml",
        "2.5 liters",
        "1 l",
        "3 cl",
        "0.75 L",
        "1 m3"
    ]
    for case in test_cases:
        try:
            result = convert_to_liters(case)
            print(f"{case} -> {result}")
        except ValueError as e:
            print(f"{case} -> Error: {e}")