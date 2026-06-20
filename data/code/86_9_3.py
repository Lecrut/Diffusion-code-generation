def compare_booleans(a: bool, b: bool) -> str:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return f"{a} is equal to {b}" if a == b else f"{a} is not equal to {b}"

if __name__ == '__main__':
    result = compare_booleans(True, False)
    print(result)