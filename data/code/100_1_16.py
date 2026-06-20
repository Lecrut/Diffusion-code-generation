def check_logic(A, B, C):
    intermediate_result = B or not C
    final_result = A and intermediate_result
    return final_result

if __name__ == '__main__':
    A_val = False
    B_val = True
    C_val = False
    result = check_logic(A_val, B_val, C_val)
    print(result)