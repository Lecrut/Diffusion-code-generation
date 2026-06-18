def compare_distances(unit1=None, value1=0, unit2=None, value2=0):
    def parse_input(value, unit):
        if isinstance(value, (int, float)):
            return value * 1e-6                                      
        elif hasattr(value, 'value') and hasattr(unit, 'name'):
            return value.value / get_conversion_factor(unit.name)
        else:
            raise ValueError("Invalid input format")
    def get_conversion_factor(u):
        factors = {
            "m": 1.0,
            "km": 1e3,
            "cm": 1e-2,
            "mm": 1e-3,
            "um": 1e-6,
            "nm": 1e-9,
        }
        return factors.get(u.lower(), 1.0)
    try:
        base_val_1 = parse_input(value1, unit1) if not isinstance(value1, (int, float)) else value1 * get_conversion_factor(unit1 or "m")
        base_val_2 = parse_input(value2, unit2) if not isinstance(value2, (int, float)) else value2 * get_conversion_factor(unit2 or "m")
        diff = abs(base_val_1 - base_val_2)
        return {
            "distance_diff": diff,
            "unit_used_for_comparison": "micrometers",
            "input_values_original": [value1 if isinstance(value1, (int, float)) else f"{value1} in {unit1}", value2 if isinstance(value2, (int, float)) else f"{value2} in {unit2}"]
        }
    except Exception as e:
        return {"error": str(e)}
if __name__ == '__main__':
    result = compare_distances(unit1="km", value1=50.5, unit2="m", value2=3)
    print(result["distance_diff"])