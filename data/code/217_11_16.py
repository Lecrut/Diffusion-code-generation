def validate_inputs(a: int, b: int) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError('Both inputs must be integers.')
    return True

def calculate_operations(a: int, b: int) -> dict:
    if not validate_inputs(a, b):
        return {}
    operations = {'addition': a + b, 'subtraction': a - b, 'multiplication': a * b, 'division': a / b if b != 0 else None}
    return operations
if __name__ == '__main__':
    result1 = calculate_operations(10, 5)
    print(result1)
    result2 = calculate_operations(7, 7)
    print(result2)