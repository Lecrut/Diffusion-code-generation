def repeating_pattern_generator():
    pattern = 'ABC'
    while True:
        for char in pattern:
            yield char

if __name__ == '__main__':
    gen = repeating_pattern_generator()
    for _ in range(30):
        print(next(gen), end='')