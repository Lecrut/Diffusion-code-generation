import numpy as np

class LogicGates:

    def AND(self, a, b):
        if isinstance(a, list) and isinstance(b, list):
            return [x & y for x, y in zip(a, b)]
        else:
            return a & b

    def OR(self, a, b):
        if isinstance(a, list) and isinstance(b, list):
            return [x | y for x, y in zip(a, b)]
        else:
            return a | b

    def NOT(self, a):
        if isinstance(a, list):
            return [~x & 1 for x in a]
        else:
            return ~a & 1
if __name__ == '__main__':
    lg = LogicGates()
    print(lg.AND([0, 1, 1], [1, 0, 1]))
    print(lg.OR([0, 1, 1], [1, 0, 1]))
    print(lg.NOT([0, 1]))