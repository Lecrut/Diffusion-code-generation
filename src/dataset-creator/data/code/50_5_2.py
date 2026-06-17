def add_three_variables(a: float, b: float, c: float) -> float:
    try:
        return a + b + c
    except TypeError as e:
        raise ValueError("All inputs must be numeric.") from e
if __name__ == '__main__':
    result = add_three_variables(1.5, 2.0, 3.5)
    print(result)