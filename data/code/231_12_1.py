def yield_pattern(k):
    pattern = '123'
    for _ in range(k):
        yield pattern

if __name__ == '__main__':
    result = list(yield_pattern(5))
    print(result)