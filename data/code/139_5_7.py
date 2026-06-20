import numpy as np

class LogicGates:

    def AND(self, a, b):
        if isinstance(a, (list, np.ndarray)) and isinstance(b, (list, np.ndarray)):
            return [x & y for x, y in zip(a, b)]
        else:
            return a & b

    def OR(self, a, b):
        if isinstance(a, (list, np.ndarray)) and isinstance(b, (list, np.ndarray)):
            return [x | y for x, y in zip(a, b)]
        else:
            return a | b

    def NOT(self, a):
        if isinstance(a, (list, np.ndarray)):
            return [~x for x in a]
        else:
            return ~a
if __name__ == '__main__':
    logic_gates = LogicGates()
    print(logic_gates.AND([0, 1], [1, 1]))
    print(logic_gates.OR([0, 1], [1, 1]))
    print(logic_gates.NOT([0, 1]))