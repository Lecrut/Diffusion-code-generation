def repeating_pattern_generator():
    while True:
        yield 'A'
        yield 'B'
        yield 'C'

if __name__ == '__main__':
    generator = repeating_pattern_generator()
    for _ in range(30):
        print(next(generator))