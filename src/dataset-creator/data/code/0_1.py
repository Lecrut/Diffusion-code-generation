def safe_compare(a: any, b: any) -> bool | None:
    try:
        return a == b
    except TypeError:
        return None
if __name__ == '__main__':
    val1 = 5.0
    val2 = "5"
    result = safe_compare(val1, val2)
    if result is not None:
        print(f"{val1} equals {val2}: {result}")
    else:
        print(f"{val1} and {val2} are incompatible types.")