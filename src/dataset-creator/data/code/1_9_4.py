def subtract_integers(a: int, b: int) -> int:
    return a - b
def subtract_floats(a: float, b: float) -> float:
    return a - b
def subtract_mixed(a: float | int, b: float | int) -> float:
    if isinstance(a, int) and isinstance(b, int):
        return float(a - b)
    elif isinstance(a, float) and isinstance(b, float):
        return a - b
    elif isinstance(a, int):
        return float(a) - b
    elif isinstance(b, int):
        return a - float(b)
    else:
        raise TypeError("Unsupported input types for mixed subtraction.")
if __name__ == '__main__':
    int_result = subtract_integers(25, 10)
    print(f"Integer Subtraction (25 - 10): {int_result}")
    float_result = subtract_floats(15.75, 8.25)
    print(f"Float Subtraction (15.75 - 8.25): {float_result}")
    mixed_int_float = subtract_mixed(100, 3.5)
    print(f"Mixed Subtraction (100 - 3.5): {mixed_int_float}")
    mixed_float_int = subtract_mixed(12.5, 5)
    print(f"Mixed Subtraction (12.5 - 5): {mixed_float_int}")
    mixed_both_float = subtract_mixed(40.5, 12.3)
    print(f"Mixed Subtraction (40.5 - 12.3): {mixed_both_float}")