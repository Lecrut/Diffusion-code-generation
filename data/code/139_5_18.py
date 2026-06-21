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
            return [~x for x in a]
        else:
            return ~a

    def XOR(self, a, b):
        if isinstance(a, list) and isinstance(b, list):
            return [x ^ y for x, y in zip(a, b)]
        else:
            return a ^ b

    def NAND(self, a, b):
        if isinstance(a, list) and isinstance(b, list):
            return [~(x & y) for x, y in zip(a, b)]
        else:
            return ~(a & b)

    def NOR(self, a, b):
        if isinstance(a, list) and isinstance(b, list):
            return [~(x | y) for x, y in zip(a, b)]
        else:
            return ~(a | b)

if __name__ == '__main__':
    lg = LogicGates()
    print(lg.AND([0, 1], [1, 0]))
    print(lg.OR([0, 1], [1, 0]))
    print(lg.NOT([0, 1]))
    print(lg.XOR([0, 1], [1, 0]))
    print(lg.NAND([0, 1], [1, 0]))
    print(lg.NOR([0, 1], [1, 0]))