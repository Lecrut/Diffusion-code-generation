def strip_tuple_whitespace(tup):
    return tuple(s.strip() for s in tup)

if __name__ == '__main__':
    sample = ("  hello  ", " world ", " python ")
    result = strip_tuple_whitespace(sample)
    print(result)