def repeat_strings(strings, M):
    return [''.join([s for _ in range(M)]) for s in strings]

if __name__ == '__main__':
    sample_strings = ["foo", "bar", "baz"]
    M = 2
    result = repeat_strings(sample_strings, M)
    print(result)