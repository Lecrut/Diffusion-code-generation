from typing import Literal
def compare_distances(value_a: float | None, value_b: float | None) -> bool:
    if not isinstance(value_a, (int, float)) or not isinstance(value_b, (int, float)):
        raise TypeError("Both values must be numeric.")
    return abs(value_a - value_b) < 1e-9
if __name__ == '__main__':
    result = compare_distances(3.000000001, 3.0)
    print(result)