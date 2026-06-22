def repeating_pattern():
    while True:
        yield from "ABC"

if __name__ == '__main__':
    pattern = repeating_pattern()
    for _ in range(30):
        print(next(pattern), end='')