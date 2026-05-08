def logic_gate(A, B, C):
    result = (A and B) or (not C)
    return result
if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    output = logic_gate(A_val, B_val, C_val)
    print(output)