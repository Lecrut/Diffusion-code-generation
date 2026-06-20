def validate_inputs(a: bool, b: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")

def compare_booleans(a: bool, b: bool) -> str:
    validate_inputs(a, b)
    return "True" if a == b else "False"

if __name__ == '__main__':
    print(compare_booleans(True, False))
    print(compare_booleans(False, False))
    print(compare_booleans(True, True))