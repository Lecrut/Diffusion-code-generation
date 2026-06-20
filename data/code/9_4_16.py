def strip_whitespace_safe(value):
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (int, float, bool)):
        return str(value).strip()
    if value is None:
        return ''
    return str(value).strip()

if __name__ == '__main__':
    print(strip_whitespace_safe('  hello world  '))
    print(strip_whitespace_safe(123))
    print(strip_whitespace_safe(None))
    print(strip_whitespace_safe([1, 2, 3]))
    print(strip_whitespace_safe('no spaces'))