class LogicGates:
    @staticmethod
    def AND(a: bool, b: bool) -> bool:
        return a & b

    @staticmethod
    def OR(a: bool, b: bool) -> bool:
        return a | b

    @staticmethod
    def NOT(a: bool) -> bool:
        return not a

    @staticmethod
    def XOR(a: bool, b: bool) -> bool:
        return a ^ b

if __name__ == '__main__':
    print(LogicGates.AND(True, False))
    print(LogicGates.OR(False, True))
    print(LogicGates.NOT(True))
    print(LogicGates.XOR(True, True))