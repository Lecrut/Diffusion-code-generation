class LogicGates:
    @staticmethod
    def logic_and(a: bool, b: bool) -> bool:
        return a & b

    @staticmethod
    def logic_or(a: bool, b: bool) -> bool:
        return a | b

    @staticmethod
    def logic_not(a: bool) -> bool:
        return not a

if __name__ == '__main__':
    lg = LogicGates()
    print(f"AND(True, False): {lg.logic_and(True, False)}")
    print(f"OR(False, True): {lg.logic_or(False, True)}")
    print(f"NOT(True): {lg.logic_not(True)}")