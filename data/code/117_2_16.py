SUBTRACTION_THRESHOLD = 0.01

def subtract_numbers(a: float, b: float) -> float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers")
    return a - b

if __name__ == '__main__':
    result = subtract_numbers(15.75, 3.25)
    print(result)