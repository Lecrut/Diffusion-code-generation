def compare_booleans(a: bool, b: bool) -> tuple[bool, str]:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Both inputs must be boolean values.')
    result = a == b
    operation = '=='
    return (result, operation)
if __name__ == '__main__':
    try:
        print(compare_booleans(True, True))
        print(compare_booleans(True, False))
        print(compare_booleans(False, False))
        print(compare_booleans(False, True))
        print(compare_booleans(1, 0))
    except ValueError as e:
        print(e)