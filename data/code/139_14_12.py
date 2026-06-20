class LogicGates:

    @staticmethod
    def AND(a: bool, b: bool) -> bool:
        return a and b

    @staticmethod
    def OR(a: bool, b: bool) -> bool:
        return a or b

    @staticmethod
    def NOT(a: bool) -> bool:
        return not a

    @staticmethod
    def XOR(a: bool, b: bool) -> bool:
        return a and (not b) or (not a and b)

    @staticmethod
    def NAND(a: bool, b: bool) -> bool:
        return not LogicGates.AND(a, b)

    @staticmethod
    def NOR(a: bool, b: bool) -> bool:
        return not LogicGates.OR(a, b)
if __name__ == '__main__':
    logic = LogicGates()
    print(logic.AND(True, False))
    print(logic.OR(False, True))
    print(logic.NOT(True))
    print(logic.XOR(True, True))
    print(logic.NAND(True, True))
    print(logic.NOR(True, False))