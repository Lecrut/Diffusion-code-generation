def add_two_numbers(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return a + b

if __name__ == '__main__':
    result = add_two_numbers(7.25, 3.75)
    print(result)