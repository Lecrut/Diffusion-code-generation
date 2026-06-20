class LogicGates:
    @staticmethod
    def logic_and(a: bool, b: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Inputs must be boolean")
        return a & b

    @staticmethod
    def logic_or(a: bool, b: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Inputs must be boolean")
        return a | b

    @staticmethod
    def logic_not(a: bool) -> bool:
        if not isinstance(a, bool):
            raise ValueError("Input must be boolean")
        return ~a & 1

if __name__ == '__main__':
    logic = LogicGates()
    print(f"AND(True, False): {logic.logic_and(True, False)}")
    print(f"OR(False, True): {logic.logic_or(False, True)}")
    print(f"NOT(True): {logic.logic_not(True)}")