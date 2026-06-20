def strip_whitespace_safely(value):
    if isinstance(value, str):
        return value.strip()
    raise TypeError("Input must be a string")

if __name__ == '__main__':
    print(strip_whitespace_safely("  hello world  "))
    print(strip_whitespace_safely("no_spaces"))
    try:
        strip_whitespace_safely(123)
    except TypeError as e:
        print(str(e))