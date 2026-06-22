def repeating_pattern():
    while True:
        for char in 'ABC':
            yield char

if __name__ == '__main__':
    pattern = repeating_pattern()
    for _ in range(30):
        print(next(pattern))