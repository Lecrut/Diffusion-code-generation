def check_logic(A, B, C):
    if not isinstance(A, bool) or not isinstance(B, bool) or not isinstance(C, bool):
        raise ValueError("Inputs must be boolean types")
    
    not_c = not C
    b_or_not_c = B or not_c
    result = A and b_or_not_c
    return result

if __name__ == '__main__':
    sample_A = True
    sample_B = False
    sample_C = True
    computed_result = check_logic(sample_A, sample_B, sample_C)
    print(computed_result)