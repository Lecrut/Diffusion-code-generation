def strip_tuple_strings(tup):
    return tuple(s.strip() for s in tup)

if __name__ == '__main__':
    original = ("  hello  ", "world  ", "  python ")
    result = strip_tuple_strings(original)
    print(result)