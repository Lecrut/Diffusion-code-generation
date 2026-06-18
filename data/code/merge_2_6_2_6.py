import math
def compare_integers(a: int, b: int) -> bool:
    return a > b
def compare_floats(a: float, b: float) -> bool:
    if not (math.isinf(a) or math.isnan(a)):
        if not (math.isinf(b) or math.isnan(b)):
            return a > b
    if math.isposinf(a):
        return True
    elif math.isneginf(a):
        return False
def compare_strings(a: str, b: str) -> bool:
    try:
        return a > b
    except TypeError:
        raise ValueError("String comparison requires both arguments to be strings.")
class ComparisonModule:
    @staticmethod
    def check_greater(value_a, value_b):
        if isinstance(value_a, int) and isinstance(value_b, int):
            return compare_integers(value_a, value_b)
        elif isinstance(value_a, float) and isinstance(value_b, float):
            return compare_floats(value_a, value_b)
        elif isinstance(value_a, str) and isinstance(value_b, str):
            return compare_strings(value_a, value_b)
        else:
            raise TypeError(f"Unsupported types for comparison: {type(value_a)} and {type(value_b)}. Supported: int, float, str.")
if __name__ == '__main__':
    test_cases = [
        (10, 5),
        (-3.5, -2.1),
        ("zebra", "apple"),
        ("banana", "cherry")
    ]
    for a, b in test_cases:
        result = ComparisonModule.check_greater(a, b)
        print(f"{a} > {b}: {result}")