def AND(A: bool, B: bool) -> bool:
    return A & B

def OR(A: bool, B: bool) -> bool:
    return A | B

def NOT(A: bool) -> bool:
    return not A

if __name__ == '__main__':
    A_val = True
    B_val = False
    print(f"A={A_val}, B={B_val}, AND: {AND(A_val, B_val)}")
    print(f"A={A_val}, B={B_val}, OR: {OR(A_val, B_val)}")
    print(f"A={A_val}, NOT: {NOT(A_val)}")