def validate_booleans(a: bool, b: bool) -> None:
    if not isinstance(a, bool):
        raise ValueError("First input must be a boolean.")
    if not isinstance(b, bool):
        raise ValueError("Second input must be a boolean.")

def compare_booleans(a: bool, b: bool) -> str:
    validate_booleans(a, b)
    return f"{a} is equal to {b}" if a == b else f"{a} is not equal to {b}"

if __name__ == '__main__':
    result = compare_booleans(True, False)
    print(result)