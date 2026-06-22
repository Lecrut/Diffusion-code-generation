def repeat_strings(strings, M):
    return [s * M for s in strings]

if __name__ == '__main__':
    sample_strings = ["apple", "banana"]
    M = 2
    result = repeat_strings(sample_strings, M)
    print(result)