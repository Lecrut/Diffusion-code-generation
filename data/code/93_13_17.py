def validate_inputs(a: bool, b: bool) -> None:
    if not isinstance(a, bool):
        raise ValueError("First input must be a boolean.")
    if not isinstance(b, bool):
        raise ValueError("Second input must be a boolean.")

def both_false(a: bool, b: bool) -> bool:
    validate_inputs(a, b)
    return not a and not b

if __name__ == '__main__':
    x = False
    y = False
    result = both_false(x, y)
    print(result)