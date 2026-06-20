def validate_inputs(a: bool, b: bool) -> None:
    if not isinstance(a, bool):
        raise ValueError("First input must be a boolean")
    if not isinstance(b, bool):
        raise ValueError("Second input must be a boolean")

def compare_booleans(a: bool, b: bool) -> bool:
    validate_inputs(a, b)
    return a == b

if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(False, False))
    print(compare_booleans(True, False))