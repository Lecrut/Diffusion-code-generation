import numpy as np

class LogicGates:

    def AND(self, a, b):
        if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
            return np.bitwise_and(a, b)
        elif isinstance(a, list) and isinstance(b, list):
            return [x & y for x, y in zip(a, b)]
        else:
            return a & b

    def OR(self, a, b):
        if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
            return np.bitwise_or(a, b)
        elif isinstance(a, list) and isinstance(b, list):
            return [x | y for x, y in zip(a, b)]
        else:
            return a | b

    def NOT(self, a):
        if isinstance(a, np.ndarray):
            return np.bitwise_not(a) & 1
        elif isinstance(a, list):
            return [~x & 1 for x in a]
        else:
            return ~a & 1
if __name__ == '__main__':
    logic = LogicGates()
    print(logic.AND([0, 1], [1, 0]))
    print(logic.OR([0, 1], [1, 0]))
    print(logic.NOT([0, 1]))