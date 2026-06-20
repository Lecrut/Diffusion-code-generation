def validate_input(a: bool, b: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Both inputs must be boolean values.')

def xnor(a: bool, b: bool) -> bool:
    validate_input(a, b)
    return a == b
if __name__ == '__main__':
    result1 = xnor(True, True)
    print(result1)
    result2 = xnor(False, False)
    print(result2)
    result3 = xnor(True, False)
    print(result3)
    result4 = xnor(False, True)
    print(result4)