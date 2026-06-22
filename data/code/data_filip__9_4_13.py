def strip_whitespace_safely(value):
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (int, float, bool)):
        return str(value).strip()
    if value is None:
        return ''
    return str(value).strip()

if __name__ == '__main__':
    print(strip_whitespace_safely('  hello world  '))
    print(strip_whitespace_safely(42))
    print(strip_whitespace_safely(None))
    print(strip_whitespace_safely(3.14))
    print(strip_whitespace_safely(True))
    print(strip_whitespace_safely([1, 2, 3]))