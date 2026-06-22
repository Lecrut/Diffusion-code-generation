def repeat_strings(strings, M):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the list must be strings")
    if not isinstance(M, int) or M < 0:
        raise ValueError("M must be a non-negative integer")
    
    return [s * M for s in strings]

if __name__ == '__main__':
    sample_strings = ["hello", "world"]
    M = 3
    result = repeat_strings(sample_strings, M)
    print(result)