def convert_to_liters(volume_str: str) -> float:
    import re
    volume = 0.0
    unit_multiplier = 1.0
    valid_units = ['l', 'litre', 'liter', 'milliliter', 'ml']
    match = re.match(r'^([\d\.]+)\s*(.*)$', volume_str.strip(), re.IGNORECASE)
    if not match:
        raise ValueError("Invalid input format")
    try:
        value = float(match.group(1))
    except ValueError:
        raise ValueError(f"Cannot convert {match.group(1)} to a number")
    unit_part = match.group(2).strip().lower() if match.group(2) else 'l'
    for v_unit in valid_units:
        if unit_part == v_unit or (len(unit_part) > len(v_unit) and unit_part.startswith(v_unit)):
            multiplier_map = {
                'ml': 0.001,
                'litre': 1.0,
                'liter': 1.0,
                'l': 1.0
            }
            if v_unit in ['milliliter', 'ml']:
                unit_multiplier = multiplier_map[v_unit]
            else:
                unit_multiplier = multiplier_map.get(unit_part, 1.0)
            break
    return value * unit_multiplier
if __name__ == '__main__':
    test_cases = [
        "5",
        "2.5 l",
        "100 ml",
        "3 litre",
        "7 liter"
    ]
    for case in test_cases:
        result = convert_to_liters(case)
        print(f"{case} -> {result}")