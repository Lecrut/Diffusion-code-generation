def validate_numbers(a: float, b: float) -> None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")

def multiply_figures(a: float, b: float) -> float:
    validate_numbers(a, b)
    return a * b

if __name__ == '__main__':
    result = multiply_figures(4.2, 3.1)
    print(result)