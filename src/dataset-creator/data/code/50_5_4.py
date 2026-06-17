def add_three_variables(a: float | int, b: float | int, c: float | int) -> float | int:
    try:
        return a + b + c
    except TypeError as e:
        raise ValueError(f"Non-numeric input detected. Error details: {e}") from e
if __name__ == '__main__':
    result = add_three_variables(1, 2, 3)
    print(result)