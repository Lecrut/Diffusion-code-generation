def count_digits(s: str) -> int:
    return sum(c.isdigit() for c in s)

if __name__ == '__main__':
    print(count_digits("a1b2c3"))