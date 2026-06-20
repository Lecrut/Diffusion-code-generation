def AND(A: bool, B: bool) -> bool:
    return A & B

def OR(A: bool, B: bool) -> bool:
    return A | B

def NOT(A: bool) -> bool:
    return not A

if __name__ == '__main__':
    A_val = True
    B_val = False
    print(f"A={A_val}, B={B_val}")
    print(f"AND({A_val}, {B_val}): {AND(A_val, B_val)}")
    print(f"OR({A_val}, {B_val}): {OR(A_val, B_val)}")
    print(f"NOT({A_val}): {NOT(A_val)}")
    print(f"NOT({B_val}): {NOT(B_val)}")