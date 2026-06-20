def strip_whitespace_in_tuple(tuple_input):
    cleaned = tuple(s.strip() for s in tuple_input)
    return cleaned

if __name__ == '__main__':
    original = ("  hello  ", " world ", "foo")
    result = strip_whitespace_in_tuple(original)
    print(result)