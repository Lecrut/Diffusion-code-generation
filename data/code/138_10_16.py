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
    return not ((A and not B) or (not A and B))

if __name__ == '__main__':
    print("A | B | AND")
    print("---|---|-----")
    for A in [True, False]:
        for B in [True, False]:
            result = AND(A, B)
            print(f"{A} | {B} | {result}")

    print("\nA | B | OR")
    print("---|---|----")
    for A in [True, False]:
        for B in [True, False]:
            result = OR(A, B)
            print(f"{A} | {B} | {result}")

    print("\nA | NOT(A)")
    print("---|---------")
    for A in [True, False]:
        result = NOT(A)
        print(f"{A} | {result}")

    print("\nA | B | NAND")
    print("---|---|------")
    for A in [True, False]:
        for B in [True, False]:
            result = NAND(A, B)
            print(f"{A} | {B} | {result}")

    print("\nA | B | NOR")
    print("---|---|-----")
    for A in [True, False]:
        for B in [True, False]:
            result = NOR(A, B)
            print(f"{A} | {B} | {result}")

    print("\nA | B | XOR")
    print("---|---|----")
    for A in [True, False]:
        for B in [True, False]:
            result = XOR(A, B)
            print(f"{A} | {B} | {result}")

    print("\nA | B | XNOR")
    print("---|---|-----")
    for A in [True, False]:
        for B in [True, False]:
            result = XNOR(A, B)
            print(f"{A} | {B} | {result}")