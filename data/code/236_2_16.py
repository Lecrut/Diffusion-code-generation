def repeat_pattern(pattern, n):
    return [item for _ in range(n) for item in pattern]

if __name__ == '__main__':
    sample_tuple = ("a", "b", "c")
    repetitions = 10
    result = repeat_pattern(sample_tuple, repetitions)
    print(result)