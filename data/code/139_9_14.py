class LogicGates:

    @staticmethod
    def logic_and(a, b):
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError('Inputs must be boolean')
        return a & b

    @staticmethod
    def logic_or(a, b):
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError('Inputs must be boolean')
        return a | b

    @staticmethod
    def logic_not(a):
        if not isinstance(a, bool):
            raise ValueError('Input must be boolean')
        return ~a + 1
if __name__ == '__main__':
    a_val = True
    b_val = False
    print(f'AND({a_val}, {b_val}): {LogicGates.logic_and(a_val, b_val)}')
    print(f'OR({a_val}, {b_val}): {LogicGates.logic_or(a_val, b_val)}')
    print(f'NOT({a_val}): {LogicGates.logic_not(a_val)}')
    a_val = False
    b_val = False
    print(f'AND({a_val}, {b_val}): {LogicGates.logic_and(a_val, b_val)}')
    print(f'OR({a_val}, {b_val}): {LogicGates.logic_or(a_val, b_val)}')
    print(f'NOT({a_val}): {LogicGates.logic_not(a_val)}')