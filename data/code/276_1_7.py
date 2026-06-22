def repeat_strings(strings, M):
    return [s * M for s in strings]

if __name__ == '__main__':
    SAMPLE_STRINGS = ["hello", "world"]
    M = 3
    result = repeat_strings(SAMPLE_STRINGS, M)
    print(result)