def subtract_integers(a: int, b: int) -> int:
    return a - b
def subtract_floats(a: float, b: float) -> float:
    return a - b
def subtract_mixed(a: float, b: int) -> float:
    return a - float(b)
if __name__ == '__main__':
    int_result = subtract_integers(25, 10)
    print(f"Integer Subtraction (25 - 10): {int_result}")
    float_result = subtract_floats(15.75, 4.25)
    print(f"Float Subtraction (15.75 - 4.25): {float_result}")
    mixed_result = subtract_mixed(100.5, 30)
    print(f"Mixed Subtraction (100.5 - 30): {mixed_result}")