def repeat_strings(strings, M):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in strings must be strings")
    if not isinstance(M, int) or M < 1:
        raise ValueError("M must be a positive integer")

    return [s * M for s in strings]

if __name__ == '__main__':
    sample_strings = ["hello", "world"]
    M = 3
    result = repeat_strings(sample_strings, M)
    print(result)