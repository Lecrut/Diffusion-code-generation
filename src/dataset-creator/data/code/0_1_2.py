def safe_compare(a: any, b: any) -> bool | None:
    try:
        return a == b
    except TypeError:
        return None
if __name__ == '__main__':
    val1 = "hello"
    val2 = 456
    result = safe_compare(val1, val2)
    if result is not None:
        print(f"{val1} equals {val2}: {result}")
    else:
        print("Comparison failed due to incompatible types.")