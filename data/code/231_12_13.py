PATTERN = '123'

def yield_pattern(k):
    index = 0
    while k > 0:
        yield PATTERN[index]
        index = (index + 1) % len(PATTERN)
        k -= 1

if __name__ == '__main__':
    sample_count = 8
    result = list(yield_pattern(sample_count))
    print(result)