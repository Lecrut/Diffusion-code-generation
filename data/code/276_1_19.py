def repeat_strings(strings, M):
    def validate_input():
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise ValueError("strings must be a list of strings")
        if not isinstance(M, int) or M < 0:
            raise ValueError("M must be a non-negative integer")

    validate_input()
    return [s * M for s in strings]

if __name__ == '__main__':
    sample_strings = ["hello", "world"]
    M = 3
    result = repeat_strings(sample_strings, M)
    print(result)