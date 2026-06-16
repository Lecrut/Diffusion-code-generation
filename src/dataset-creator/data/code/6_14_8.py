import operator as op
def safe_gt(a: any, b: any) -> bool | None:
    try:
        return op.gt(a, b)
    except TypeError:
        raise ValueError("Inputs must be numeric") from None
if __name__ == '__main__':
    a = 10.5
    b = 3
    result_a_b = safe_gt(a, b)
    c = "not a number"
    d = 20
    try:
        result_c_d = safe_gt(c, d)
    except ValueError as e:
        print(f"Error comparing {c} and {d}: {e}")
    assert result_a_b is True, "10.5 should be greater than 3"