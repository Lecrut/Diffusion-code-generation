class LogicGates:
    TRUE = 1
    FALSE = 0

    @staticmethod
    def AND(a, b):
        return a & b

    @staticmethod
    def OR(a, b):
        return a | b

    @staticmethod
    def NOT(a):
        return not a & 1

    @staticmethod
    def XOR(a, b):
        return a ^ b

    @staticmethod
    def NAND(a, b):
        return ~(a & b)

    @staticmethod
    def NOR(a, b):
        return ~(a | b)

    @staticmethod
    def XNOR(a, b):
        return ~(a ^ b)

if __name__ == '__main__':
    print(LogicGates.AND(True, False))
    print(LogicGates.OR(False, True))
    print(LogicGates.NOT(True))