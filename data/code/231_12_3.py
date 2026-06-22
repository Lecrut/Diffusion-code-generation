def yield_pattern(k):
    pattern = '123'
    for _ in range(k):
        for char in pattern:
            yield char

if __name__ == '__main__':
    result = list(yield_pattern(9))
    print(result)