def check_logic(A, B, C):
    not_c = not C
    b_or_not_c = B or not_c
    final_result = A and b_or_not_c
    return final_result

if __name__ == '__main__':
    val_a = False
    val_b = True
    val_c = False
    output = check_logic(val_a, val_b, val_c)
    print(output)