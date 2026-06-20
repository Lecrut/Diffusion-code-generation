def AND(A, B):
    return A and B

def OR(A, B):
    return A or B

def NOT(A):
    return not A

def NAND(A, B):
    return not (A and B)

def NOR(A, B):
    return not (A or B)

def XOR(A, B):
    return (A or B) and not (A and B)

def XNOR(A, B):
    return (A and B) or (not A and not B)

if __name__ == '__main__':
    A = [0, 1]
    B = [0, 1]
    print("A | B | A AND B | A OR B | NOT A | A NAND B | A NOR B | A XOR B | A XNOR B")
    print("-"*55)
    for i in range(len(A)):
        and_result = AND(A[i], B[i])
        or_result = OR(A[i], B[i])
        not_a = NOT(A[i])
        nand_result = NAND(A[i], B[i])
        nor_result = NOR(A[i], B[i])
        xor_result = XOR(A[i], B[i])
        xnor_result = XNOR(A[i], B[i])
        print(f"{A[i]} | {B[i]} | {and_result} | {or_result} | {not_a} | {nand_result} | {nor_result} | {xor_result} | {xnor_result}")