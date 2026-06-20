def and_op(a, b):
    return a and b

def or_op(a, b):
    return a or b

def not_op(a):
    return not a

def nand_op(a, b):
    return not (a and b)

def nor_op(a, b):
    return not (a or b)

def xor_op(a, b):
    return (a or b) and not (a and b)

def xnor_op(a, b):
    return not ((a or b) and not (a and b))

if __name__ == '__main__':
    A = [True, False]
    B = [True, False]

    print("A | B | AND")
    print("---|---|-----")
    for a in A:
        for b in B:
            result = and_op(a, b)
            print(f"{a} | {b} | {result}")

    print("\nA | B | OR")
    print("---|---|----")
    for a in A:
        for b in B:
            result = or_op(a, b)
            print(f"{a} | {b} | {result}")

    print("\nA | NOT(A)")
    print("---|--------")
    for a in A:
        result = not_op(a)
        print(f"{a} | {result}")

    print("\nA | B | NAND")
    print("---|---|------")
    for a in A:
        for b in B:
            result = nand_op(a, b)
            print(f"{a} | {b} | {result}")

    print("\nA | B | NOR")
    print("---|---|-----")
    for a in A:
        for b in B:
            result = nor_op(a, b)
            print(f"{a} | {b} | {result}")

    print("\nA | B | XOR")
    print("---|---|----")
    for a in A:
        for b in B:
            result = xor_op(a, b)
            print(f"{a} | {b} | {result}")

    print("\nA | B | XNOR")
    print("---|---|-----")
    for a in A:
        for b in B:
            result = xnor_op(a, b)
            print(f"{a} | {b} | {result}")