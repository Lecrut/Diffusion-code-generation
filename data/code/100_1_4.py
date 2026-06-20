def check_logic(A, B, C):
    intermediate = B or not C
    result = A and intermediate
    return result

if __name__ == '__main__':
    A_val = False
    B_val = True
    C_val = True
    output = check_logic(A_val, B_val, C_val)
    print(output)