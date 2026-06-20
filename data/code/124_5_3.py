from typing import Union

def compute_operations(a: int, b: int) -> dict:
    return {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b if b != 0 else None,
        'modulus': a % b if b != 0 else None
    }

if __name__ == '__main__':
    a = 100
    b = 7
    results = compute_operations(a, b)
    print(f"Addition: {results['add']}")
    print(f"Subtraction: {results['subtract']}")
    print(f"Multiplication: {results['multiply']}")
    print(f"Division: {results['divide']}")
    print(f"Modulus: {results['modulus']}")