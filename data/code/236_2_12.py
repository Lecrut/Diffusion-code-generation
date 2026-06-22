def repeat_pattern(pattern, n):
    if not isinstance(pattern, tuple) or not all(isinstance(item, str) for item in pattern):
        raise ValueError("Pattern must be a tuple of strings")
    if not isinstance(n, int) or n < 0:
        raise ValueError("Repeat count must be a non-negative integer")

    repeated = [item for _ in range(n) for item in pattern]
    return repeated

if __name__ == '__main__':
    sample_pattern = ("###", "###", "###")
    repeat_count = 10
    result = repeat_pattern(sample_pattern, repeat_count)
    print(result)