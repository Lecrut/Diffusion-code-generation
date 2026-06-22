def calculate_operations(a: int, b: int) -> dict:
    operations = {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': a / b if b != 0 else None
    }
    return operations

if __name__ == '__main__':
    result1 = calculate_operations(10, 5)
    print(result1)
    result2 = calculate_operations(7, 7)
    print(result2)
    result3 = calculate_operations(20, 0)
    print(result3)