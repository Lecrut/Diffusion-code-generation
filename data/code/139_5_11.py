import numpy as np

class LogicGates:

    def AND(self, a, b):
        if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
            return np.bitwise_and(a, b)
        else:
            return a & b

    def OR(self, a, b):
        if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
            return np.bitwise_or(a, b)
        else:
            return a | b

    def NOT(self, a):
        if isinstance(a, np.ndarray):
            return np.invert(a)
        else:
            return ~a
if __name__ == '__main__':
    logic = LogicGates()
    print(logic.AND(0, 1))
    print(logic.OR(0, 1))
    print(logic.NOT(0))
    a = np.array([0, 1])
    b = np.array([1, 0])
    print(logic.AND(a, b))
    print(logic.OR(a, b))
    print(logic.NOT(a))