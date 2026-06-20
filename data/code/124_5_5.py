from typing import Tuple

def compute_results(a: int, b: int) -> Tuple[int, float]:
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return addition, subtraction, multiplication, division

if __name__ == '__main__':
    a = 100
    b = 7
    results = compute_results(a, b)
    print(f"Addition: {results[0]}")
    print(f"Subtraction: {results[1]}")
    print(f"Multiplication: {results[2]}")
    print(f"Division: {results[3]:.2f}")