from typing import Literal
def compare_distance(
    distance_a: float | None = 0.0,
    distance_b: float | None = 0.0,
) -> tuple[Literal["equal", "a_greater", "b_greater"], int]:
    if not isinstance(distance_a, (int, float)) or not isinstance(distance_b, (int, float)):
        raise TypeError("Both arguments must be numeric.")
    diff = distance_a - distance_b
    is_equal = abs(diff) < 1e-9
    return ("equal" if is_equal else "a_greater", int(abs(diff)))
if __name__ == '__main__':
    result, difference = compare_distance(5.0, 3.2)
    print(f"{result}: {difference}")