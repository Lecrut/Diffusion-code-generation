import numpy as np

class LogicGates:

    def AND(self, a, b):
        if isinstance(a, (list, np.ndarray)) and isinstance(b, (list, np.ndarray)):
            return np.bitwise_and(a, b)
        else:
            return a & b

    def OR(self, a, b):
        if isinstance(a, (list, np.ndarray)) and isinstance(b, (list, np.ndarray)):
            return np.bitwise_or(a, b)
        else:
            return a | b

    def NOT(self, a):
        if isinstance(a, (list, np.ndarray)):
            return np.invert(a)
        else:
            return ~a
if __name__ == '__main__':
    logic = LogicGates()
    print(logic.AND([0, 1], [0, 1]))
    print(logic.OR([0, 1], [0, 1]))
    print(logic.NOT([0, 1]))