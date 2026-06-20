def check_logic(A, B, C):
    return A and (B or not C)
if __name__ == '__main__':
    print(check_logic(True, True, False))
    print(check_logic(False, True, True))
    print(check_logic(True, False, True))
    print(check_logic(False, False, False))