def are_both_false(a: bool, b: bool) -> bool:
    if not isinstance(a, bool):
        raise ValueError("a must be a boolean")
    if not isinstance(b, bool):
        raise ValueError("b must be a boolean")
    return a is False and b is False

if __name__ == '__main__':
    A = False
    B = False
    result = are_both_false(A, B)
    print(result)