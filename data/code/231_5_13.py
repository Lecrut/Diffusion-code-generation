def repeating_pattern():
    while True:
        yield 'A'
        yield 'B'
        yield 'C'

if __name__ == '__main__':
    pattern = repeating_pattern()
    for _ in range(30):
        print(next(pattern))