def validate_inputs(a: bool, b: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Inputs must be boolean values.')

def compare_booleans(a: bool, b: bool) -> bool:
    validate_inputs(a, b)
    return a == b
if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(True, False))
    print(compare_booleans(False, False))
    print(compare_booleans(False, True))