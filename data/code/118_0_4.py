def multiply_figures(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers.")
    return a * b

if __name__ == '__main__':
    result = multiply_figures(3.5, 2.0)
    print(result)