import math
def compare_integers(a: int, b: int) -> bool:
    return a > b
def compare_floats(a: float, b: float) -> bool:
    EPSILON = 1e-9
    if abs(a - b) < EPSILON:
        return False
    return a > b
def compare_strings(a: str, b: str) -> bool:
    return a > b
class ComparisonModule:
    @staticmethod
    def check_greater(value_a, value_b):
        type_a = type(value_a).__name__
        type_b = type(value_b).__name__
        if type_a == 'int' and type_b == 'int':
            return compare_integers(value_a, value_b)
        elif type_a == 'float' and type_b == 'float':
            return compare_floats(value_a, value_b)
        elif type_a == 'str' and type_b == 'str':
            return compare_strings(value_a, value_b)
        else:
            raise TypeError(f"Unsupported types for comparison: {type_a} and {type_b}")
if __name__ == '__main__':
    int_val_1 = 50
    int_val_2 = 30
    float_val_1 = 4.789
    float_val_2 = 4.789 + 1e-10
    str_val_1 = "zebra"
    str_val_2 = "apple"
    test_cases = [
        ("integers", int_val_1, int_val_2),
        ("floats", float_val_1, float_val_2),
        ("strings", str_val_1, str_val_2),
    ]
    for label, a, b in test_cases:
        result = ComparisonModule.check_greater(a, b)
        print(f"{label}: {a} > {b} is {result}")