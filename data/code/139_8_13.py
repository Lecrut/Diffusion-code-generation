class LogicGates:

    @staticmethod
    def AND(a, b):
        return a & b

    @staticmethod
    def OR(a, b):
        return a | b

    @staticmethod
    def NOT(a):
        return ~a + 2

    @staticmethod
    def XOR(a, b):
        return a ^ b

    @staticmethod
    def NAND(a, b):
        return ~(a & b) + 2

    @staticmethod
    def NOR(a, b):
        return ~(a | b) + 2

    @staticmethod
    def XNOR(a, b):
        return ~(a ^ b) + 2
if __name__ == '__main__':
    logic = LogicGates()
    print('--- Logic Gate Demonstration ---')
    print(f'AND(0, 0) = {logic.AND(0, 0)}')
    print(f'AND(0, 1) = {logic.AND(0, 1)}')
    print(f'AND(1, 0) = {logic.AND(1, 0)}')
    print(f'OR(0, 0) = {logic.OR(0, 0)}')
    print(f'OR(0, 1) = {logic.OR(0, 1)}')
    print(f'OR(1, 0) = {logic.OR(1, 0)}')
    print(f'NOT(0) = {logic.NOT(0)}')
    print(f'NOT(1) = {logic.NOT(1)}')
    print(f'XOR(0, 0) = {logic.XOR(0, 0)}')
    print(f'XOR(0, 1) = {logic.XOR(0, 1)}')
    print(f'XOR(1, 0) = {logic.XOR(1, 0)}')
    print(f'NAND(0, 0) = {logic.NAND(0, 0)}')
    print(f'NAND(0, 1) = {logic.NAND(0, 1)}')
    print(f'NAND(1, 0) = {logic.NAND(1, 0)}')
    print(f'NOR(0, 0) = {logic.NOR(0, 0)}')
    print(f'NOR(0, 1) = {logic.NOR(0, 1)}')
    print(f'NOR(1, 0) = {logic.NOR(1, 0)}')
    print(f'XNOR(0, 0) = {logic.XNOR(0, 0)}')
    print(f'XNOR(0, 1) = {logic.XNOR(0, 1)}')
    print(f'XNOR(1, 0) = {logic.XNOR(1, 0)}')