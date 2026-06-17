def calculate_sum(a: float, b: float, c: float) -> float:
    try:
        return a + b + c
    except TypeError as e:
        raise ValueError("All arguments must be numeric.") from e
if __name__ == '__main__':
    val_a = 10.5
    val_b = 20.3
    val_c = 30.7
    result = calculate_sum(val_a, val_b, val_c)
    print(result)