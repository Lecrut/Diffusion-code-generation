def calculate_operations(a: int, b: int) -> dict:
    return {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': a / b if b != 0 else None
    }

if __name__ == '__main__':
    result1 = calculate_operations(10, 5)
    print(f"Operations on 10 and 5: {result1}")
    result2 = calculate_operations(7, 7)
    print(f"Operations on 7 and 7: {result2}")
    result3 = calculate_operations(20, 30)
    print(f"Operations on 20 and 30: {result3}")