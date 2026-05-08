if __name__ == '__main__':
    A = 10
    B = 5
    C = 3
    result_and = A & B
    not_C = ~C
    result_or = result_and | not_C
    xor_result = (A ^ B) ^ (C ^ C) ^ (A & B)                                              
    result = (A & B) | (~C)
    X_and_Y = A & B
    not_C_val = ~C
    final_xor_not_result = (~(~(A ^ B))) | not_C_val
    print(final_xor_not_result)