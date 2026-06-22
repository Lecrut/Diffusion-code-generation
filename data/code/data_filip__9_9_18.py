def strip_whitespace_from_tuple(t):
    return tuple(s.strip() for s in t)

if __name__ == '__main__':
    sample = ("  hello ", "world  ", "  foo bar  ", "   ")
    print(strip_whitespace_from_tuple(sample))