class LogicGates:
    @staticmethod
    def logic_and(a: bool, b: bool) -> bool:
        return a & b

    @staticmethod
    def logic_or(a: bool, b: bool) -> bool:
        return a | b

    @staticmethod
    def logic_not(a: bool) -> bool:
        return ~a

if __name__ == '__main__':
    gates = LogicGates()
    print(f"AND(True, False): {gates.logic_and(True, False)}")
    print(f"OR(False, True): {gates.logic_or(False, True)}")
    print(f"NOT(True): {gates.logic_not(True)}")