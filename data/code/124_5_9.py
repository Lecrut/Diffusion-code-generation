from typing import Union

def compute_results(a: int, b: int) -> dict:
    return {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': a / b if b != 0 else None,
        'integer_division': a // b if b != 0 else None,
        'modulus': a % b if b != 0 else None
    }

if __name__ == '__main__':
    a = 100
    b = 7
    results = compute_results(a, b)
    print(results)