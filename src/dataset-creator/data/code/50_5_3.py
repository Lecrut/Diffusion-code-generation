def add_three_variables(a: float, b: float, c: float) -> float:
    try:
        return a + b + c
    except TypeError as e:
        raise ValueError(f"Invalid input types for addition: {e}") from e
if __name__ == '__main__':
    result = add_three_variables(10.5, 20.3, 30.4)
    print(result)