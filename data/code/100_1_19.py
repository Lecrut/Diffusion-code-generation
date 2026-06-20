def check_logic(A, B, C):
    return A and (B or not C)

if __name__ == '__main__':
    TRUE = True
    FALSE = False

    A_val = TRUE
    B_val = FALSE
    C_val = TRUE

    result = check_logic(A_val, B_val, C_val)
    print(result)