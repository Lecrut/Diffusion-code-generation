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
    a_val = True
    b_val = False
    print(f"AND({a_val}, {b_val}): {LogicGates.logic_and(a_val, b_val)}")
    print(f"OR({a_val}, {b_val}): {LogicGates.logic_or(a_val, b_val)}")
    print(f"NOT({a_val}): {LogicGates.logic_not(a_val)}")