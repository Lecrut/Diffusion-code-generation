from typing import Tuple

def calculate(a: int, b: int) -> Tuple[int, float]:
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else None
    return addition, subtraction, multiplication, division

if __name__ == '__main__':
    a = 100
    b = 7
    result = calculate(a, b)
    print(f"Addition: {result[0]}")
    print(f"Subtraction: {result[1]}")
    print(f"Multiplication: {result[2]}")
    if result[3] is not None:
        print(f"Division: {result[3]:.2f}")
    else:
        print("Division by zero error")