def and_gate(A: bool, B: bool) -> bool:
    return A & B

def or_gate(A: bool, B: bool) -> bool:
    return A | B

def not_gate(A: bool) -> bool:
    return ~A + 1

if __name__ == '__main__':
    A_val = True
    B_val = False
    print(f"A={A_val}, B={B_val}, AND: {and_gate(A_val, B_val)}")
    print(f"A={A_val}, B={B_val}, OR: {or_gate(A_val, B_val)}")
    print(f"A={A_val}, NOT: {not_gate(A_val)}")