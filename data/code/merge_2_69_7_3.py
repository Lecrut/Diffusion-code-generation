import re
def parse_mass_string(input_str):
    units = {
        'kg': 1,
        'g': 0.001,
        'mg': 1e-6,
        't': 1000,
        'lb': 0.45359237,
        'oz': 0.028349523125
    }
    pattern = r'^([+-]?\d*\.?\d+)\s*(kg|g|mg|t|lb|oz)$'
    match = re.match(pattern, input_str.strip())
    if not match:
        raise ValueError(f"Invalid format. Expected numeric value followed by unit (e.g., '5 kg').")
    try:
        mass_value = float(match.group(1))
    except ValueError:
        raise ValueError("First part of the string must be a valid number.")
    selected_unit = match.group(2).lower()
    if selected_unit not in units:
        raise ValueError(f"Unsupported unit '{selected_unit}'. Supported units: {', '.join(units.keys())}")
    return mass_value * units[selected_unit]
if __name__ == '__main__':
    test_cases = [
        "10 kg",
        "5 g",
        "-3 mg",
        "2 t",
        "4.5 lb",
        "8 oz"
    ]
    for case in test_cases:
        try:
            result_kg = parse_mass_string(case)
            print(f"{case} -> {result_kg:.6f} kg")
        except ValueError as e:
            print(f"Error processing '{case}': {e}")