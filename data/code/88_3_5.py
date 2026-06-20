def validate_inputs(a: bool, b: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")

def check_conditions_met(a: bool, b: bool) -> bool:
    validate_inputs(a, b)
    return a and b

if __name__ == '__main__':
    print(check_conditions_met(True, True))
    print(check_conditions_met(False, True))
    print(check_conditions_met(True, False))
    print(check_conditions_met(False, False))