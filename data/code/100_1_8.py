def check_logic(A, B, C):
    if not isinstance(A, bool) or not isinstance(B, bool) or not isinstance(C, bool):
        raise ValueError("All inputs must be boolean values.")
    return A and (B or not C)

if __name__ == '__main__':
    result = check_logic(True, False, True)
    print(result)