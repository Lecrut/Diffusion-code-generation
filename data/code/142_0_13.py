def compare_booleans(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    return a == b

if __name__ == '__main__':
    try:
        result = compare_booleans(True, False)
        print(result)
    except ValueError as e:
        print(e)