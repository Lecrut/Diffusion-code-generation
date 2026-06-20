def AND(A: bool, B: bool) -> bool:
    return A & B

def OR(A: bool, B: bool) -> bool:
    return A | B

def NOT(A: bool) -> bool:
    return not A

if __name__ == '__main__':
    A_val = False
    B_val = True
    result_and = AND(A_val, B_val)
    print(f"A={A_val}, B={B_val}, AND: {result_and}")
    result_or = OR(A_val, B_val)
    print(f"A={A_val}, B={B_val}, OR: {result_or}")
    result_not = NOT(A_val)
    print(f"A={A_val}, NOT: {result_not}")