import sys
def compare_values(a: object, b: object) -> bool | None:
    try:
        return a == b
    except TypeError as e:
        print(f"Error comparing values of type {type(a).__name__} and {type(b).__name__}: {e}", file=sys.stderr)
        return None
if __name__ == '__main__':
    val1 = 42.5
    val2 = "42.5"
    result = compare_values(val1, val2)
    if result is not None:
        print(f"{val1} == {val2}: {result}")
    else:
        print("Comparison failed due to type incompatibility.")