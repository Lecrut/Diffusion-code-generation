def strip_whitespace_safely(value):
    if not isinstance(value, str):
        return None
    return value.strip()

if __name__ == '__main__':
    sample_string = "  hello world  "
    sample_int = 42
    sample_none = None
    sample_list = [1, 2, 3]

    print(strip_whitespace_safely(sample_string))
    print(strip_whitespace_safely(sample_int))
    print(strip_whitespace_safely(sample_none))
    print(strip_whitespace_safely(sample_list))