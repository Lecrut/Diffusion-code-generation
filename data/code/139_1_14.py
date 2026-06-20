import operator

class LogicGateSystem:
    AND = operator.and_
    OR = operator.or_
    NOT = operator.not_
    XOR = operator.xor

    @staticmethod
    def and_(a, b):
        return LogicGateSystem.AND(a, b)

    @staticmethod
    def or_(a, b):
        return LogicGateSystem.OR(a, b)

    @staticmethod
    def not_(a):
        return LogicGateSystem.NOT(a)

    @staticmethod
    def xor_(a, b):
        return LogicGateSystem.XOR(a, b)

if __name__ == '__main__':
    print(f"AND: {LogicGateSystem.and_(1, 0)}")
    print(f"OR: {LogicGateSystem.or_(1, 0)}")
    print(f"NOT 1: {LogicGateSystem.not_(1)}")
    print(f"XOR: {LogicGateSystem.xor_(1, 0)}")