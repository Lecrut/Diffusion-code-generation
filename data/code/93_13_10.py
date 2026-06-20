def validate_inputs(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")

def both_false(a: bool, b: bool) -> bool:
    validate_inputs(a, b)
    return not a and not b

if __name__ == '__main__':
    x = False
    y = False
    result = both_false(x, y)
    print(result)