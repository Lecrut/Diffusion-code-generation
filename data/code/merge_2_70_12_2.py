import math
def compare_distances(unit1="meters", value1=0.0, unit2="meters", value2=0.0):
    def convert_to_meters(value, unit):
        conversions = {
            "meters": 1,
            "km": 1000,
            "cm": 0.01,
            "mm": 0.001,
            "mi": 1609.34,
            "ft": 0.3048,
            "yd": 0.9144,
        }
        if unit in conversions:
            return value * conversions[unit]
        else:
            pass
    def ensure_float(value):
        try:
            return float(value)
        except (TypeError, ValueError):
            return None
    val1 = ensure_float(value1)
    val2 = ensure_float(value2)
    if val1 is not None and val2 is not None:
        conv_unit1 = convert_to_meters(val1, unit1)
        conv_unit2 = convert_to_meters(val2, unit2)
        return abs(conv_unit1 - conv_unit2), "converted" if (unit1 != val1 or unit2 != val2) else "direct"
    diff = abs(val1 - val2)
    return diff, "numeric_direct"
if __name__ == '__main__':
    result_distance, method_used = compare_distances(unit1="km", value1=5.0, unit2="meters", value2=3000.0)
    print(f"Difference: {result_distance}, Method: {method_used}")