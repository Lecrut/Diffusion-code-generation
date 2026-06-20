def validate_inputs(a: bool, b: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values")

def check_conditions(a: bool, b: bool) -> bool:
    validate_inputs(a, b)
    return (a and not b) or (not a and b)

if __name__ == '__main__':
    print(check_conditions(True, False))
    print(check_conditions(False, True))
    print(check_conditions(True, True))
    print(check_conditions(False, False))