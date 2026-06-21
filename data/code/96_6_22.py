def compute_bitwise_logic(A, B, C, D):
    val_a = 1 if A else 0
    val_b = 1 if B else 0
    val_c = 1 if C else 0
    val_d = 1 if D else 0
    term_one = val_a & val_b
    term_two = val_c & (1 - val_d)
    final_result = term_one | term_two
    return final_result

if __name__ == '__main__':
    A = 0
    B = 1
    C = 1
    D = 1
    output = compute_bitwise_logic(A, B, C, D)
    print(output)