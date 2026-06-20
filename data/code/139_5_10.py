import numpy as np

class LogicGates:

    @staticmethod
    def AND(a, b):
        if isinstance(a, (list, np.ndarray)) and isinstance(b, (list, np.ndarray)):
            return np.bitwise_and(a, b)
        else:
            return a & b

    @staticmethod
    def OR(a, b):
        if isinstance(a, (list, np.ndarray)) and isinstance(b, (list, np.ndarray)):
            return np.bitwise_or(a, b)
        else:
            return a | b

    @staticmethod
    def NOT(a):
        if isinstance(a, (list, np.ndarray)):
            return np.invert(a)
        else:
            return ~a

    @staticmethod
    def XOR(a, b):
        if isinstance(a, (list, np.ndarray)) and isinstance(b, (list, np.ndarray)):
            return np.bitwise_xor(a, b)
        else:
            return a ^ b
if __name__ == '__main__':
    logic = LogicGates()
    print(logic.AND([0, 1, 1], [1, 0, 1]))
    print(logic.OR([0, 1, 1], [1, 0, 1]))
    print(logic.NOT([0, 1]))
    print(logic.XOR([0, 1, 1], [1, 0, 1]))