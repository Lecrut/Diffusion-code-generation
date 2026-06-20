def validate_inputs(a: bool, b: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both arguments must be boolean values.")

def compare_booleans(a: bool, b: bool) -> bool:
    validate_inputs(a, b)
    return a == b

if __name__ == '__main__':
    result1 = compare_booleans(True, True)
    print(result1)
    result2 = compare_booleans(True, False)
    print(result2)