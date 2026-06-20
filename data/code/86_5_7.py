def validate_inputs(a: bool, b: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")

def compare_booleans(a: bool, b: bool) -> tuple:
    validate_inputs(a, b)
    return (a == b), '=='

if __name__ == '__main__':
    result = compare_booleans(True, False)
    print(result)