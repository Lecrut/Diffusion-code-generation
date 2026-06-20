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
    gate_system = LogicGateSystem()
    print(f"AND(1, 0): {gate_system.AND(1, 0)}")
    print(f"OR(1, 0): {gate_system.OR(1, 0)}")
    print(f"NOT(1): {gate_system.NOT(1)}")
    print(f"XOR(1, 0): {gate_system.XOR(1, 0)}")