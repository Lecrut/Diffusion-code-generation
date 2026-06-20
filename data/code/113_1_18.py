def validate_inputs(a: int, b: int) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    return True

def subtract_values(a: int, b: int) -> int:
    if validate_inputs(a, b):
        return a - b

if __name__ == '__main__':
    fixed_value1 = 10
    fixed_value2 = 3
    result = subtract_values(fixed_value1, fixed_value2)
    print(result)