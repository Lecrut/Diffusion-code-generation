class LogicGates:
    @staticmethod
    def validate_input(a, b):
        if not (isinstance(a, bool) and isinstance(b, bool)):
            raise ValueError("Both inputs must be boolean values")

    @staticmethod
    def logic_and(a, b):
        LogicGates.validate_input(a, b)
        return a & b

    @staticmethod
    def logic_or(a, b):
        LogicGates.validate_input(a, b)
        return a | b

    @staticmethod
    def logic_not(a):
        LogicGates.validate_input(a, None)
        return ~a

if __name__ == '__main__':
    a_val = True
    b_val = False
    print(f"AND({a_val}, {b_val}): {LogicGates.logic_and(a_val, b_val)}")
    print(f"OR({a_val}, {b_val}): {LogicGates.logic_or(a_val, b_val)}")
    print(f"NOT({a_val}): {LogicGates.logic_not(a_val)}")
    a_val = True
    b_val = True
    print(f"AND({a_val}, {b_val}): {LogicGates.logic_and(a_val, b_val)}")
    print(f"OR({a_val}, {b_val}): {LogicGates.logic_or(a_val, b_val)}")
    print(f"NOT({a_val}): {LogicGates.logic_not(a_val)}")