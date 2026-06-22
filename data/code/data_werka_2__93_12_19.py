def verify_false_state(a: bool, b: bool) -> bool:
    if not isinstance(a, bool):
        raise ValueError("Argument a must be a boolean type")
    if not isinstance(b, bool):
        raise ValueError("Argument b must be a boolean type")
    return not bool(a) and not bool(b)

if __name__ == '__main__':
    A = False
    B = False
    output = verify_false_state(A, B)
    print(output)