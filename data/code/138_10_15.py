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
    return (A and not B) or (not A and B)

def XNOR(A, B):
    return (A and B) or (not A and not B)

if __name__ == '__main__':
    A = [True, False]
    B = [False, True]
    print("A | B | A AND B")
    print("---|---|---------")
    for i in range(len(A)):
        result_and = AND(A[i], B[i])
        print(f"{A[i]} | {B[i]} | {result_and}")