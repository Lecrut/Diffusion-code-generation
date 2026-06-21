TRUE_CONSTANT = True
FALSE_CONSTANT = False

def check_logic(A, B, C):
    not_c = not C
    b_or_not_c = B or not_c
    result = A and b_or_not_c
    return result

if __name__ == '__main__':
    val_a = TRUE_CONSTANT
    val_b = FALSE_CONSTANT
    val_c = TRUE_CONSTANT
    output = check_logic(val_a, val_b, val_c)
    print(output)