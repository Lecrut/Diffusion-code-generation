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
    logic = LogicGateSystem()
    print(logic.AND(True, False))
    print(logic.OR(True, False))
    print(logic.NOT(True))
    print(logic.XOR(True, False))