def safe_compare(a: any, b: any) -> bool | None:
    try:
        return a == b
    except TypeError:
        return None
if __name__ == '__main__':
    val1 = 5
    val2 = "5"
    result = safe_compare(val1, val2)
    print(result if result is not None else "Types are incompatible")