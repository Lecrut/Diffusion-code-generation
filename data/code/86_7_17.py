def compare_booleans(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values")
    return a == b

if __name__ == '__main__':
    val1 = True
    val2 = True
    result1 = compare_booleans(val1, val2)
    print(f"Comparing {val1} and {val2}: {result1}")

    val3 = False
    val4 = True
    result2 = compare_booleans(val3, val4)
    print(f"Comparing {val3} and {val4}: {result2}")

    val5 = False
    val6 = False
    result3 = compare_booleans(val5, val6)
    print(f"Comparing {val5} and {val6}: {result3}")