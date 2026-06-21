def validate_booleans(a: bool, b: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")

def compare_booleans(a: bool, b: bool) -> bool:
    validate_booleans(a, b)
    return a ^ b == 0

if __name__ == '__main__':
    val1 = True
    val2 = True
    result1 = compare_booleans(val1, val2)
    print(f"Comparing {val1} and {val2}: Result={result1}")

    val3 = False
    val4 = True
    result2 = compare_booleans(val3, val4)
    print(f"Comparing {val3} and {val4}: Result={result2}")