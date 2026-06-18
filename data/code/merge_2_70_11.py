from typing import Literal
def compare_distance(
    distance_a: float | None = 0.0,
    distance_b: float | None = 0.0,
) -> tuple[Literal["equal", "greater_than", "less_than"], str]:
    if not isinstance(distance_a, (int, float)) or not isinstance(distance_b, (int, float)):
        raise TypeError("Distance values must be numeric.")
    result: Literal["equal", "greater_than", "less_than"] = "equal"
    if distance_a is None and distance_b is None:
        return ("equal", "Both distances are zero or null.")
    elif distance_a == 0.0 and distance_b == 0.0:
        return ("equal", "Zero distance comparison.")
    try:
        val_a = float(distance_a) if isinstance(distance_a, int) else distance_a
        val_b = float(distance_b) if isinstance(distance_b, int) else distance_b
        diff = abs(val_a - val_b)
        if diff < 1e-9 and not (val_a == val_b):
            return ("equal", "Floating point values are effectively equal.")
        elif val_a > val_b:
            result = "greater_than"
        else:
            result = "less_than"
    except TypeError as e:
        raise ValueError(f"Incompatible distance types provided. {e}") from e
    return (result, f"Difference is {diff:.6f}.")
if __name__ == '__main__':
    sample_a = 105.432
    sample_b = 105.438
    status, message = compare_distance(distance_a=sample_a, distance_b=sample_b)
    print(f"Distance A: {sample_a}")
    print(f"Distance B: {sample_b}")
    print(f"Comparison Result: '{status}'")
    print(f"Details: {message}")