from typing import Tuple

def compute_results(a: int, b: int) -> Tuple[int, float, str]:
    addition = a + b
    subtraction = a - b
    division = a / b if b != 0 else 'undefined'
    return addition, subtraction, division

if __name__ == '__main__':
    a, b = 100, 7
    results = compute_results(a, b)
    print(f"Addition: {results[0]}")
    print(f"Subtraction: {results[1]}")
    print(f"Division: {results[2]}")