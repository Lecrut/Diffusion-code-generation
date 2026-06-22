def repeat_tuple_pattern(pattern):
    return [item for _ in range(10) for item in pattern]

if __name__ == '__main__':
    sample_pattern = (1, 2, 3)
    result = repeat_tuple_pattern(sample_pattern)
    print(result)