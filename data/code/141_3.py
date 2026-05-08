def and_or_not_gate(A, B, C):
    return (A and B) or (not A or C)
if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    result = and_or_not_gate(A_val, B_val, C_val)
    print(result)