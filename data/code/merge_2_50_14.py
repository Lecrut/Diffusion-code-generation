def compute_sum(a: float, b: float, c: float) -> None:
    try:
        result = a + b + c
        print(result)
    except TypeError as e:
        raise ValueError("All inputs must be numeric.") from e
if __name__ == '__main__':
    val_a = 10.5
    val_b = 20.3
    val_c = -5.7
    compute_sum(val_a, val_b, val_c)