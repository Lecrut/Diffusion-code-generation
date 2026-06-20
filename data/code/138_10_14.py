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
    return a and (not b) or (not a and b)

def XNOR(a, b):
    return a and b or (not a and (not b))
if __name__ == '__main__':
    A = [False, False, True, True]
    B = [False, True, False, True]
    print('A | B | A AND B | A OR B | NOT A | A NAND B | A NOR B | A XOR B | A XNOR B')
    print('-' * 40)
    for i in range(len(A)):
        and_result = AND(A[i], B[i])
        or_result = OR(A[i], B[i])
        not_a = NOT(A[i])
        nand_result = NAND(A[i], B[i])
        nor_result = NOR(A[i], B[i])
        xor_result = XOR(A[i], B[i])
        xnor_result = XNOR(A[i], B[i])
        print(f'{A[i]} | {B[i]} | {and_result} | {or_result} | {not_a} | {nand_result} | {nor_result} | {xor_result} | {xnor_result}')