def check_logic(A, B, C):
    if not A:
        return False
    if B or not C:
        return True
    return False

if __name__ == '__main__':
    print(check_logic(True, True, False))
    print(check_logic(True, False, True))
    print(check_logic(False, True, False))
    print(check_logic(False, False, True))