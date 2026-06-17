def compute_sum(a: float, b: float, c: float) -> None:
    try:
        sum_result = a + b + c
        print(f"Sum of {a}, {b}, and {c} is {sum_result}")
    except TypeError as e:
        raise ValueError("All inputs must be numeric.") from e
if __name__ == '__main__':
    val1 = 10.5
    val2 = 20.3
    val3 = 49.7
    compute_sum(val1, val2, val3)