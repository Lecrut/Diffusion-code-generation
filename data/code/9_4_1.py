def strip_whitespace_safely(value):
    if not isinstance(value, str):
        return value
    return value.strip()

if __name__ == '__main__':
    print(strip_whitespace_safely("  hello world  "))
    print(strip_whitespace_safely(123))
    print(strip_whitespace_safely(None))
    print(strip_whitespace_safely(["  list  "]))