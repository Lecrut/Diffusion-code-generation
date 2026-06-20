def multiply_numbers(a: float, b: float) -> float:
    try:
        return float(a) * float(b)
    except ValueError:
        raise ValueError("Both inputs must be numeric")

if __name__ == '__main__':
    result = multiply_numbers(3.5, 2.0)
    print(result)