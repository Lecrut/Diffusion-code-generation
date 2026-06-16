import operator as op
def safe_gt(a: any, b: any) -> bool | None:
    try:
        return op.gt(a, b)
    except TypeError:
        raise ValueError("Inputs must be numeric.") from None
if __name__ == '__main__':
    result1 = safe_gt(5.0, 3.0)
    print(f"Result for (5.0, 3.0): {result1}")
    try:
        result2 = safe_gt("a", "b")
    except ValueError as e:
        print(f"Caught expected error: {e}")