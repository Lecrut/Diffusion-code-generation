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
    logic = LogicGates()
    print('AND(0, 1):', logic.AND(0, 1))
    print('OR(0, 1):', logic.OR(0, 1))
    print('NOT([0, 1]):', logic.NOT([0, 1]))