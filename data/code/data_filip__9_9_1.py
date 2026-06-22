def strip_whitespace_tuple(t: tuple) -> tuple:
    return tuple(s.strip() for s in t)

if __name__ == '__main__':
    sample = ("  hello  ", " world ", "python  ", "  data  ")
    result = strip_whitespace_tuple(sample)
    print(result)