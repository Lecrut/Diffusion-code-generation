def strip_whitespace_from_tuple(strings: tuple) -> tuple:
    return tuple(s.strip() for s in strings)

if __name__ == '__main__':
    sample = ("  hello  ", " world ", "\tnew\n", "  python  ")
    result = strip_whitespace_from_tuple(sample)
    print(result)