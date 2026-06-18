def compare_integers(a: int, b: int) -> bool:
    return a > b
def compare_floats(a: float, b: float) -> bool:
    if not (a == a and b == b):
        raise ValueError("NaN values detected")
    return a > b
def compare_strings(a: str, b: str) -> bool:
    return a > b
class ComparisonModule:
    @staticmethod
    def check_greater(type_a: type, value_a, type_b: type, value_b):
        if type_a == int and type_b == int:
            return compare_integers(value_a, value_b)
        elif type_a == float and type_b == float:
            return compare_floats(value_a, value_b)
        elif type_a == str and type_b == str:
            return compare_strings(value_a, value_b)
        else:
            raise TypeError(f"Unsupported types for comparison: {type_a} vs {type_b}")
if __name__ == '__main__':
    print(compare_integers(10, 5))
    print(compare_floats(3.14, 2.71))
    print(compare_strings("zebra", "apple"))
    result = ComparisonModule.check_greater(int, 99, int, 88)
    print(result)