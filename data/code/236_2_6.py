def repeat_tuple_pattern(pattern, n):
    if not isinstance(pattern, tuple) or not isinstance(n, int):
        raise ValueError("Invalid input: pattern must be a tuple and n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    repeated = [item for _ in range(n) for item in pattern]
    return repeated

if __name__ == '__main__':
    sample_pattern = (1, 2, 3)
    repeat_count = 10
    result = repeat_tuple_pattern(sample_pattern, repeat_count)
    print(result)