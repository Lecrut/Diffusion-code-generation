def count_digits(s):
    return sum(c.isdigit() for c in s)

if __name__ == '__main__':
    print(count_digits("a1b2c3"))
    print(count_digits("hello"))
    print(count_digits("12345"))
    print(count_digits("abc123def456"))