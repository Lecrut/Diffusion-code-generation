def perform_operations(x: int, y: int) -> dict:
    result = {
        'sum': x + y,
        'difference': x - y,
        'product': x * y,
        'quotient': x / y if y != 0 else None
    }
    return result

if __name__ == '__main__':
    a = 15
    b = 3
    ops_result = perform_operations(a, b)
    print(f"Operations with {a} and {b}: {ops_result}")