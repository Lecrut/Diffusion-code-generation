def yield_pattern(k):
    pattern = '123'
    index = 0
    for _ in range(k):
        yield pattern[index]
        index = (index + 1) % len(pattern)

if __name__ == '__main__':
    sample_count = 15
    result = list(yield_pattern(sample_count))
    print(result)