from typing import Tuple

def compute_arithmetic(a: int, b: int) -> Tuple[int, int, int]:
    addition = a + b
    multiplication = a * b
    division_floor = a // b if b != 0 else 0
    return addition, multiplication, division_floor

if __name__ == '__main__':
    a = 100
    b = 7
    result = compute_arithmetic(a, b)
    print(f"Addition: {result[0]}")
    print(f"Multiplication: {result[1]}")
    print(f"Division (Floor): {result[2]}")