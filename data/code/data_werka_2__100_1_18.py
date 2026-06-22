def check_logic(A, B, C):
    op_map = {
        (True, True): lambda x: x,
        (True, False): lambda x: not x,
        (False, True): lambda x: x,
        (False, False): lambda x: x,
    }
    not_c = op_map[(C, False)](C)
    b_or_not_c = B or not_c
    result = A and b_or_not_c
    return result

if __name__ == '__main__':
    sample_A = True
    sample_B = False
    sample_C = True
    output = check_logic(sample_A, sample_B, sample_C)
    print(output)