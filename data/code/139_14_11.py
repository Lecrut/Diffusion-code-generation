def AND(a: bool, b: bool) -> bool:
    return a and b

def OR(a: bool, b: bool) -> bool:
    return a or b

def NOT(a: bool) -> bool:
    return not a

def XOR(a: bool, b: bool) -> bool:
    return (a and not b) or (not a and b)

def NAND(a: bool, b: bool) -> bool:
    return not AND(a, b)

def NOR(a: bool, b: bool) -> bool:
    return not OR(a, b)

if __name__ == '__main__':
    sample_a = True
    sample_b = False

    print("AND:", AND(sample_a, sample_b))
    print("OR:", OR(sample_a, sample_b))
    print("NOT a:", NOT(sample_a))
    print("XOR:", XOR(sample_a, sample_b))
    print("NAND:", NAND(sample_a, sample_b))
    print("NOR:", NOR(sample_a, sample_b))