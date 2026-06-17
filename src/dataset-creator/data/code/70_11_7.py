from typing import Literal
def compare_distances(value_a: float | None, value_b: float | None) -> bool:
    if not isinstance(value_a, (int, float)) or not isinstance(value_b, (int, float)):
        raise TypeError("Both values must be numeric.")
    return value_a == value_b
if __name__ == '__main__':
    result = compare_distances(10.5, 10.5)
    print(result if result else "Values differ")