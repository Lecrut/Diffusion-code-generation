def yield_pattern(k):
    pattern = '123'
    for _ in range(k):
        yield pattern

if __name__ == '__main__':
    sample_count = 10
    result = list(yield_pattern(sample_count))
    print(result)