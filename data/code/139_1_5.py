import operator

class LogicGateSystem:

    @staticmethod
    def AND(a, b):
        return operator.and_(a, b)

    @staticmethod
    def OR(a, b):
        return operator.or_(a, b)

    @staticmethod
    def NOT(a):
        return operator.not_(a)

    @staticmethod
    def XOR(a, b):
        return operator.xor(a, b)
if __name__ == '__main__':
    logic_gate = LogicGateSystem()
    print(logic_gate.AND(True, False))
    print(logic_gate.OR(True, False))
    print(logic_gate.NOT(True))
    print(logic_gate.XOR(True, False))