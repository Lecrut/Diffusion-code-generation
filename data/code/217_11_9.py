def calculate_operations(a: int, b: int) -> dict:
    return {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': a / b if b != 0 else float('inf')
    }

if __name__ == '__main__':
    result = calculate_operations(10, 5)
    print(result)