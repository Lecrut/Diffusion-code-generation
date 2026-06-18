import sys
def convert_mass(value_str):
    try:
        value = float(value_str)
    except ValueError:
        return None
    unit_map = {
        'kg': 1,
        'g': 0.001,
        'mg': 1e-6,
        't': 1000,
        'lb': 0.45359237,
    }
    unit = value_str.split()[1].lower() if len(value_str.split()) > 1 else 'kg'
    return round(value * unit_map.get(unit.lower(), None), 6)
if __name__ == '__main__':
    test_cases = [
        "5 kg",
        "200 g",
        "3 mg",
        "1 t",
        "10 lb"
    ]
    for case in test_cases:
        result = convert_mass(case)
        if result is not None:
            print(f"{case} -> {result}")