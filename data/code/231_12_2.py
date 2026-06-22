def yield_pattern(k):
    pattern = '123'
    index = 0
    while k > 0:
        yield pattern[index]
        index = (index + 1) % len(pattern)
        k -= 1

if __name__ == '__main__':
    sample_count = 8
    result = list(yield_pattern(sample_count))
    print(result)