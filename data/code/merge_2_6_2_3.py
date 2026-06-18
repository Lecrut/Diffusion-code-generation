import math
def compare_integers(a: int, b: int) -> bool:
    return a > b
def compare_floats(a: float, b: float) -> bool:
    if not (math.isinf(a) or math.isnan(a)) and not (math.isinf(b) or math.isnan(b)):
        return a > b
    elif math.isinf(a):
        if math.copysign(math.inf, a) == 1.0:
            return True
        else:
            return False
    elif math.isnan(a):
        return False
def compare_strings(a: str, b: str) -> bool:
    try:
        return a > b
    except TypeError:
        raise ValueError("Both arguments must be strings")
class ValueComparator:
    @staticmethod
    def is_greater(value_a, value_b):
        if isinstance(value_a, int) and isinstance(value_b, int):
            return compare_integers(value_a, value_b)
        elif isinstance(value_a, float) and isinstance(value_b, float):
            return compare_floats(value_a, value_b)
        elif isinstance(value_a, str) and isinstance(value_b, str):
            return compare_strings(value_a, value_b)
        else:
            raise TypeError("Unsupported data types for comparison")
if __name__ == '__main__':
    test_cases = [
        (10, 5),
        (-3.5, -2.1),
        ("banana", "apple"),
        ("zebra", "ant"),
        (float('inf'), float('-inf')),
        (math.nan, 1.0)
    ]
    for a, b in test_cases:
        try:
            result = ValueComparator.is_greater(a, b)
            print(f"{a} > {b}: {result}")
        except Exception as e:
            print(f"Error comparing {a} and {b}: {e}")