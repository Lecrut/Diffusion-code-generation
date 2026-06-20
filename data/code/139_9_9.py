class LogicGates:
    @staticmethod
    def and_gate(a: bool, b: bool) -> bool:
        return a & b

    @staticmethod
    def or_gate(a: bool, b: bool) -> bool:
        return a | b

    @staticmethod
    def not_gate(a: bool) -> bool:
        return ~a & 1

if __name__ == '__main__':
    logic = LogicGates()
    print(f"AND(True, False): {logic.and_gate(True, False)}")
    print(f"OR(False, True): {logic.or_gate(False, True)}")
    print(f"NOT(True): {logic.not_gate(True)}")