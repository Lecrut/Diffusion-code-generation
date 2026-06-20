AND = lambda A, B: A & B
OR = lambda A, B: A | B
NOT = lambda A: ~A + 2

def logic_gates(A, B, C):
    and_result = AND(AND(A, B), C)
    or_result = OR(OR(A, B), C)
    not_A = NOT(A)
    not_B = NOT(B)
    not_C = NOT(C)
    return {'AND': and_result, 'OR': or_result, 'NOT_A': not_A, 'NOT_B': not_B, 'NOT_C': not_C}
if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    results = logic_gates(A_val, B_val, C_val)
    print(results)