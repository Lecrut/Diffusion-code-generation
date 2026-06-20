def add_two_numbers(a: float, b: float) -> float:
    if not (isinstance(a, float) and isinstance(b, float)):
        raise ValueError("Both inputs must be floating-point numbers.")
    return a + b

if __name__ == '__main__':
    try:
        result1 = add_two_numbers(5.0, 3.2)
        print(result1)
        result2 = add_two_numbers(-10.5, 20.7)
        print(result2)
    except ValueError as e:
        print(e)