from operator import gt as is_gt
def safe_compare(a: any, b: any) -> bool | None:
    try:
        return is_gt(a, b)
    except TypeError:
        raise ValueError(f"Non-numeric comparison attempted between {type(a).__name__} and {type(b).__name__}")
if __name__ == '__main__':
    result = safe_compare(10.5, 3.2)
    print(result if isinstance(result, bool) else "Comparison failed")
    try:
        bad_result = safe_compare("a", "b")
    except ValueError as e:
        print(f"Caught exception: {e}")