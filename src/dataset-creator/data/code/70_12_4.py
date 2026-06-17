import math
def compare_distances(unit_a=None, value_a=0, unit_b=None, value_b=0):
    def normalize(value, unit):
        if isinstance(value, float) and not (isinstance(value, str)):
            return value * 1.0
        conversion_rates = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'mi': 1609.34,
            'yd': 0.9144,
        }
        rate = conversion_rates.get(unit.lower(), 1.0) if isinstance(value, str) else value
        return float(rate * value)
    val_a = normalize(value_a, unit_a)
    val_b = normalize(value_b, unit_b)
    diff = abs(val_a - val_b)
    threshold = 1e-6
    is_equal = math.isclose(val_a, val_b, rel_tol=threshold, abs_tol=0.0) if isinstance(val_a, float) and isinstance(val_b, float) else (val_a == val_b)
    return {
        'value_a': value_a,
        'unit_a': unit_a,
        'normalized_value_a': val_a,
        'value_b': value_b,
        'unit_b': unit_b,
        'normalized_value_b': val_b,
        'difference': diff,
        'is_equal': is_equal
    }
if __name__ == '__main__':
    result = compare_distances(unit_a='km', value_a=1.5, unit_b='m', value_b=1500)
    print(f"Comparison Result: {result}")