def validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")

def compare_booleans(a: bool, b: bool) -> bool:
    validate_boolean(a)
    validate_boolean(b)
    return a == b

if __name__ == '__main__':
    result = compare_booleans(True, False)
    print(result)