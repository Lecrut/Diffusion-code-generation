class LogicGates:
    @staticmethod
    def validate_input(value):
        if not isinstance(value, bool):
            raise TypeError("Input must be a boolean")

    @staticmethod
    def logic_and(a, b):
        LogicGates.validate_input(a)
        LogicGates.validate_input(b)
        return a & b

    @staticmethod
    def logic_or(a, b):
        LogicGates.validate_input(a)
        LogicGates.validate_input(b)
        return a | b

    @staticmethod
    def logic_not(a):
        LogicGates.validate_input(a)
        return ~a

if __name__ == '__main__':
    a_val = True
    b_val = False
    print(f"AND({a_val}, {b_val}): {LogicGates.logic_and(a_val, b_val)}")
    print(f"OR({a_val}, {b_val}): {LogicGates.logic_or(a_val, b_val)}")
    print(f"NOT({a_val}): {LogicGates.logic_not(a_val)}")