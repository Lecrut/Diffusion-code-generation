def check_logic(A, B, C):
    return A and (B or not C)
if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    result = check_logic(A_val, B_val, C_val)
    print(result)