from typing import Optional
def convert_mass(value: float, from_unit: str, to_unit: str) -> dict[str, object]:
    valid_units = ['kg', 'g', 'mg']
    if value == 0 or not isinstance(value, (int, float)):
        return {
            "success": False,
            "error": f"Invalid input: Input must be a non-zero numeric type."
        }
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    if from_unit_lower not in valid_units or to_unit_lower not in valid_units:
        return {
            "success": False,
            "error": f"Invalid unit. Supported units are: kg, g, mg."
        }
    conversion_factors = {
        'kg': {'g': 1000, 'mg': 1_000_000},
        'g': {'kg': 0.001, 'mg': 1000},
        'mg': {'kg': 1e-6, 'g': 0.001}
    }
    factor = conversion_factors[from_unit_lower][to_unit_lower]
    converted_value = value * factor
    return {
        "success": True,
        "original_value": value,
        "from_unit": from_unit.lower(),
        "converted_value": rounded(converted_value),
        "to_unit": to_unit.lower()
    }
def rounded(value: float) -> int:
    return round(value, 6) if value != int(value) else int(value)
if __name__ == '__main__':
    test_cases = [
        (100, 'kg', 'g'),
        (500, 'mg', 'kg'),
        (2.5, 'g', 'mg')
    ]
    for val, from_u, to_u in test_cases:
        result = convert_mass(val, from_u, to_u)
        if not result["success"]:
            print(f"Error converting {val} {from_u}: {result['error']}")
        else:
            print(f"{val} {from_u} is equal to {result['converted_value']}{to_u}")
    edge_result = convert_mass(0, 'kg', 'g')
    if not edge_result["success"]:
        print("Edge case (zero input) handled correctly.")