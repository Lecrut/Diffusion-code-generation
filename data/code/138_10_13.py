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
    sample_values = [
        (True, True), (True, False), (False, True), (False, False)
    ]
    print("A | B | A AND B")
    print("---|---|---------")
    for A, B in sample_values:
        result_and = BooleanLogic.AND(A, B)
        print(f"{A} | {B} | {result_and}")