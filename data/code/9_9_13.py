def strip_whitespace_from_tuple(input_tuple):
    return tuple(s.strip() for s in input_tuple)

if __name__ == '__main__':
    sample_tuple = ("  hello  ", " world ", "\tfoo\n", " bar \t")
    cleaned = strip_whitespace_from_tuple(sample_tuple)
    print(cleaned)