import operator as op
def safe_greater(a: any, b: any) -> bool | None:
    try:
        return op.gt(a, b)
    except TypeError:
        raise ValueError("Inputs must be numeric.") from None
if __name__ == '__main__':
    result1 = safe_greater(5.0, 3.0)
    print(f"Result for (5, 3): {result1}")
    try:
        result2 = safe_greater("a", "b")
    except ValueError as e:
        print(f"Caught expected error: {e}")
    result3 = safe_greater(10.5, float('inf'))
    print(f"Result for (10.5, inf): {result3}")