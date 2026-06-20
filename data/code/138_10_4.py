def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def NAND(a, b):
    return not (a and b)

def NOR(a, b):
    return not (a or b)

def XOR(a, b):
    return a != b

def XNOR(a, b):
    return a == b

if __name__ == '__main__':
    print("AND:", AND(True, True), AND(True, False), AND(False, True), AND(False, False))
    print("OR:", OR(True, True), OR(True, False), OR(False, True), OR(False, False))
    print("NOT:", NOT(True), NOT(False))
    print("NAND:", NAND(True, True), NAND(True, False), NAND(False, True), NAND(False, False))
    print("NOR:", NOR(True, True), NOR(True, False), NOR(False, True), NOR(False, False))
    print("XOR:", XOR(True, True), XOR(True, False), XOR(False, True), XOR(False, False))
    print("XNOR:", XNOR(True, True), XNOR(True, False), XNOR(False, True), XNOR(False, False))