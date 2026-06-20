def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return not a

def XOR(a, b):
    return a ^ b

def NAND(a, b):
    return not a & b

def NOR(a, b):
    return not a | b

def XNOR(a, b):
    return not a ^ b

if __name__ == '__main__':
    sample1 = AND(True, False)
    sample2 = OR(False, True)
    sample3 = NOT(True)

    print(f"AND(True, False) = {sample1}")
    print(f"OR(False, True) = {sample2}")
    print(f"NOT(True) = {sample3}")