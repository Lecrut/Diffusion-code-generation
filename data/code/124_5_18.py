from typing import Tuple

def compute_operations(a: int, b: int) -> Tuple[int, float, str]:
    addition = a + b
    subtraction = a - b
    division = a / b if b != 0 else 'undefined'
    return addition, subtraction, division

if __name__ == '__main__':
    a = 100
    b = 7
    result = compute_operations(a, b)
    print(f"Addition: {result[0]}")
    print(f"Subtraction: {result[1]}")
    print(f"Division: {result[2]}")