def repeat_pattern(pattern, n):
    if not isinstance(pattern, tuple) or not all(isinstance(item, str) for item in pattern):
        raise ValueError("Pattern must be a tuple of strings")
    if not isinstance(n, int) or n < 0:
        raise ValueError("Repeat count must be a non-negative integer")

    flat_list = [item for _ in range(n) for item in pattern]
    return flat_list

if __name__ == '__main__':
    sample_pattern = ("###", "###", "###")
    repeat_count = 10
    repeated_output = repeat_pattern(sample_pattern, repeat_count)
    print(repeated_output)