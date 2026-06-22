def check_logic(A, B, C):
    not_c = not C
    b_or_not_c = B or not_c
    result = A and b_or_not_c
    return result

if __name__ == '__main__':
    sample_A = False
    sample_B = True
    sample_C = False
    output = check_logic(sample_A, sample_B, sample_C)
    print(output)