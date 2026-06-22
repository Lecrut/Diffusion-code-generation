def repeating_pattern_generator():
    pattern = ('A', 'B', 'C')
    while True:
        for char in pattern:
            yield char

if __name__ == '__main__':
    gen = repeating_pattern_generator()
    result = ''.join(next(gen) for _ in range(30))
    print(result)