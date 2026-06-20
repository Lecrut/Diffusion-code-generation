def check_logic(A, B, C):
    return A and (B or not C)

if __name__ == '__main__':
    result = check_logic(True, False, True)
    print(result)