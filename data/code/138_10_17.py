class BooleanLogic:
    @staticmethod
    def AND(A, B):
        return A and B

    @staticmethod
    def OR(A, B):
        return A or B

    @staticmethod
    def NOT(A):
        return not A

    @staticmethod
    def NAND(A, B):
        return not (A and B)

    @staticmethod
    def NOR(A, B):
        return not (A or B)

    @staticmethod
    def XOR(A, B):
        return (A and not B) or (not A and B)

    @staticmethod
    def XNOR(A, B):
        return (A and B) or (not A and not B)

if __name__ == '__main__':
    A = [True, False]
    B = [True, False]

    print("A | B | A AND B")
    print("---|---|---------")
    for a in A:
        for b in B:
            result = BooleanLogic.AND(a, b)
            print(f"{a} | {b} | {result}")

    print("\nA | B | A OR B")
    print("---|---|--------")
    for a in A:
        for b in B:
            result = BooleanLogic.OR(a, b)
            print(f"{a} | {b} | {result}")

    print("\nA | NOT A")
    print("---|------")
    for a in A:
        result = BooleanLogic.NOT(a)
        print(f"{a} | {result}")

    print("\nA | B | A NAND B")
    print("---|---|---------")
    for a in A:
        for b in B:
            result = BooleanLogic.NAND(a, b)
            print(f"{a} | {b} | {result}")

    print("\nA | B | A NOR B")
    print("---|---|--------")
    for a in A:
        for b in B:
            result = BooleanLogic.NOR(a, b)
            print(f"{a} | {b} | {result}")

    print("\nA | B | A XOR B")
    print("---|---|---------")
    for a in A:
        for b in B:
            result = BooleanLogic.XOR(a, b)
            print(f"{a} | {b} | {result}")

    print("\nA | B | A XNOR B")
    print("---|---|----------")
    for a in A:
        for b in B:
            result = BooleanLogic.XNOR(a, b)
            print(f"{a} | {b} | {result}")