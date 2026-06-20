class LogicGates:
    def AND(self, a: bool, b: bool) -> bool:
        return a and b

    def OR(self, a: bool, b: bool) -> bool:
        return a or b

    def NOT(self, a: bool) -> bool:
        return not a

    def XOR(self, a: bool, b: bool) -> bool:
        return a ^ b

    def NAND(self, a: bool, b: bool) -> bool:
        return not (a and b)

    def NOR(self, a: bool, b: bool) -> bool:
        return not (a or b)

if __name__ == '__main__':
    logic = LogicGates()
    print(logic.AND(True, False))
    print(logic.OR(False, True))
    print(logic.NOT(True))
    print(logic.XOR(True, True))
    print(logic.NAND(True, True))
    print(logic.NOR(True, True))