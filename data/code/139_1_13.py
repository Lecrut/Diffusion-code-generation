import operator

class LogicGateSystem:
    @staticmethod
    def and_(a, b):
        return operator.and_(a, b)

    @staticmethod
    def or_(a, b):
        return operator.or_(a, b)

    @staticmethod
    def not_(a):
        return operator.not_(a)

    @staticmethod
    def xor(a, b):
        return operator.xor(a, b)

if __name__ == '__main__':
    print(f"AND(1, 0): {LogicGateSystem.and_(1, 0)}")
    print(f"OR(1, 0): {LogicGateSystem.or_(1, 0)}")
    print(f"NOT(1): {LogicGateSystem.not_(1)}")
    print(f"XOR(1, 0): {LogicGateSystem.xor(1, 0)}")