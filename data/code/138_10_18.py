TRUE = True
FALSE = False

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
    print("A | B | A AND B")
    print("---|---|---------")
    for A in [TRUE, FALSE]:
        for B in [TRUE, FALSE]:
            result = AND(A, B)
            print(f"{A} | {B} | {result}")
    
    print("\nA | B | A OR B")
    print("---|---|--------")
    for A in [TRUE, FALSE]:
        for B in [TRUE, FALSE]:
            result = OR(A, B)
            print(f"{A} | {B} | {result}")
    
    print("\nA | NOT A")
    print("---|-------")
    for A in [TRUE, FALSE]:
        result = NOT(A)
        print(f"{A} | {result}")
    
    print("\nA | B | A NAND B")
    print("---|---|---------")
    for A in [TRUE, FALSE]:
        for B in [TRUE, FALSE]:
            result = NAND(A, B)
            print(f"{A} | {B} | {result}")
    
    print("\nA | B | A NOR B")
    print("---|---|--------")
    for A in [TRUE, FALSE]:
        for B in [TRUE, FALSE]:
            result = NOR(A, B)
            print(f"{A} | {B} | {result}")
    
    print("\nA | B | A XOR B")
    print("---|---|---------")
    for A in [TRUE, FALSE]:
        for B in [TRUE, FALSE]:
            result = XOR(A, B)
            print(f"{A} | {B} | {result}")
    
    print("\nA | B | A XNOR B")
    print("---|---|----------")
    for A in [TRUE, FALSE]:
        for B in [TRUE, FALSE]:
            result = XNOR(A, B)
            print(f"{A} | {B} | {result}")