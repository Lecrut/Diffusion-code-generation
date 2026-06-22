def calculate_operations(a: int, b: int) -> dict:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    
    return {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': a / b if b != 0 else None
    }

if __name__ == '__main__':
    result = calculate_operations(10, 5)
    print(result)