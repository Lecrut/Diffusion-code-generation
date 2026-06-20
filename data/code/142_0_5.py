def validate_booleans(a: bool, b: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values")

def compare_booleans(a: bool, b: bool) -> bool:
    validate_booleans(a, b)
    return a == b

if __name__ == '__main__':
    result = compare_booleans(True, False)
    print(result)