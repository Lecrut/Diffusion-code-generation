def compare_values(a: object, b: object) -> bool | None:
    try:
        result = a == b
        return result if isinstance(result, (bool)) else None
    except TypeError as e:
        print(f"Error comparing values of type {type(a)} and {type(b)}: {e}")
        return False
if __name__ == '__main__':
    val1 = 42
    val2 = "hello world"
    is_equal = compare_values(val1, val2)
    if is_equal is not None:
        print(f"{val1} equals {val2}: {is_equal}")
    else:
        print("Values are of different types and cannot be directly compared.")