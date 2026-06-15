def subtract_integers(a: int, b: int) -> int:
    return a - b
def subtract_floats(a: float, b: float) -> float:
    return a - b
def subtract_mixed(a: float, b: int) -> float:
    return a - float(b)
if __name__ == '__main__':
    int_result = subtract_integers(10, 4)
    float_result = subtract_floats(25.75, 12.3)
    mixed_result = subtract_mixed(15.5, 5)
    print(f"Integer Subtraction (10 - 4): {int_result}")
    print(f"Float Subtraction (25.75 - 12.3): {float_result}")
    print(f"Mixed Subtraction (15.5 - 5): {mixed_result}")