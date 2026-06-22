def yield_pattern(k):
    if not isinstance(k, int) or k < 0:
        raise ValueError("k must be a non-negative integer")
    
    pattern = '123'
    for _ in range(k):
        yield from pattern

if __name__ == '__main__':
    sample_count = 8
    result = list(yield_pattern(sample_count))
    print(result)