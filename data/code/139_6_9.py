class LogicGates:
    @staticmethod
    def and_gate(a, b):
        if not (isinstance(a, int) or isinstance(b, int)):
            raise TypeError("Inputs must be integers.")
        return a & b

    @staticmethod
    def or_gate(a, b):
        if not (isinstance(a, int) or isinstance(b, int)):
            raise TypeError("Inputs must be integers.")
        return a | b

    @staticmethod
    def not_gate(a):
        if not isinstance(a, int):
            raise TypeError("Input must be an integer.")
        return ~a

    @staticmethod
    def xor_gate(a, b):
        if not (isinstance(a, int) or isinstance(b, int)):
            raise TypeError("Inputs must be integers.")
        return a ^ b

if __name__ == '__main__':
    print(LogicGates.and_gate(1, 0))
    print(LogicGates.or_gate(1, 0))
    print(LogicGates.not_gate(1))
    print(LogicGates.xor_gate(1, 0))