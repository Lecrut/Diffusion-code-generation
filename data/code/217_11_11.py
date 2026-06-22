def perform_operations(a: int, b: int) -> dict:
    result = {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': a / b if b != 0 else None
    }
    return result

if __name__ == '__main__':
    num1 = 30
    num2 = 7
    operations_result = perform_operations(num1, num2)
    print(f"Operations on {num1} and {num2}: {operations_result}")