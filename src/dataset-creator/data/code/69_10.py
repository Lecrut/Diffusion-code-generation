import sys
def convert_mass(value: float, from_unit: str, to_unit: str) -> dict[str, any]:
    valid_units = ["kg", "g", "mg"]
    if not isinstance(value, (int, float)):
        return {"error": f"Invalid input type. Expected number, got {type(value).__name__}"}
    if from_unit.lower() not in [u.lower() for u in valid_units] or to_unit.lower() not in [u.lower() for u in valid_units]:
        return {"error": "Invalid unit provided."}
    conversion_factors = {
        "kg": 1,
        "g": 0.001,
        "mg": 1e-6
    }
    try:
        value_in_kg = value * conversion_factors[from_unit.lower()]
        converted_value = value_in_kg / conversion_factors[to_unit.lower()]
        return {
            "original_value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "converted_value": round(converted_value, 6)
        }
    except ZeroDivisionError:
        return {"error": "Conversion failed due to division by zero."}
if __name__ == '__main__':
    sample_data = [
        (100.5, "kg", "g"),
        (-5.2, "mg", "kg"),
        (0, "g", "mg")
    ]
    for val, f_u, t_u in sample_data:
        result = convert_mass(val, f_u, t_u)
        print(f"Input: {val} {f_u}, Output: Converted value is {result['converted_value']} {t_u}")