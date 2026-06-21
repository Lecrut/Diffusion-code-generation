def is_strictly_greater(a: int, b: int) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")
    return a > b

if __name__ == '__main__':
    sample_a = 15
    sample_b = 10
    print(is_strictly_greater(sample_a, sample_b))