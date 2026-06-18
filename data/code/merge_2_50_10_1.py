def calculate_sum(a: float, b: float, c: float) -> float:
    try:
        return a + b + c
    except TypeError as e:
        raise ValueError("All arguments must be numeric.") from e
if __name__ == '__main__':
    val1 = 10.5
    val2 = 20.3
    val3 = 30.7
    total = calculate_sum(val1, val2, val3)
    print(total)