def logic_operations(A, B, C):
    and_result = A and B and C
    or_result = A or B or C
    not_A = not A
    return and_result, or_result, not_A
if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    and_res, or_res, not_A_val = logic_operations(A_val, B_val, C_val)
    print(f"A: {A_val}, B: {B_val}, C: {C_val}")
    print(f"AND: {and_res}")
    print(f"OR: {or_res}")
    print(f"NOT A: {not_A_val}")