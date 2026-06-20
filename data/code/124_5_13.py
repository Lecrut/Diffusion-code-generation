from typing import Tuple

def compute_arithmetic_operations(a: int, b: int) -> Tuple[int, float, int]:
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return addition, subtraction, multiplication, division

if __name__ == '__main__':
    a = 100
    b = 7
    result = compute_arithmetic_operations(a, b)
    print(f"Addition: {result[0]}")
    print(f"Subtraction: {result[1]}")
    print(f"Multiplication: {result[2]}")
    print(f"Division: {result[3]:.2f}")