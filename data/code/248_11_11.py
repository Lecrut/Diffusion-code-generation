def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")

def add_floats(a: float, b: float) -> float:
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    result = add_floats(3.141592653589793, 2.718281828459045)
    print(result)