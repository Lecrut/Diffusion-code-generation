def compare_booleans(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    return a == b

if __name__ == '__main__':
    val1 = True
    val2 = False
    try:
        result1 = compare_booleans(val1, val2)
        print(f"Comparing {val1} and {val2}: {result1}")
    except ValueError as e:
        print(e)

    val3 = False
    val4 = False
    try:
        result2 = compare_booleans(val3, val4)
        print(f"Comparing {val3} and {val4}: {result2}")
    except ValueError as e:
        print(e)

    val5 = True
    val6 = True
    try:
        result3 = compare_booleans(val5, val6)
        print(f"Comparing {val5} and {val6}: {result3}")
    except ValueError as e:
        print(e)