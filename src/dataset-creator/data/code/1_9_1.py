def subtract_integers(a: int, b: int) -> int:
    return a - b
def subtract_floats(a: float, b: float) -> float:
    return a - b
def subtract_mixed(a: float, b: int) -> float:
    return a - float(b)
if __name__ == '__main__':
    int_result = subtract_integers(25, 10)
    float_result = subtract_floats(3.75, 1.25)
    mixed_result = subtract_mixed(10.5, 4)
    print(f"Integer Subtraction (25 - 10): {int_result}")
    print(f"Float Subtraction (3.75 - 1.25): {float_result}")
    print(f"Mixed Subtraction (10.5 - 4): {mixed_result}")