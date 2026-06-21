def compare_booleans(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    
    return a == b

if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(True, False))
    print(compare_booleans(False, False))
    print(compare_booleans(False, True))