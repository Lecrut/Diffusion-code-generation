import operator

class LogicGateSystem:
    AND = operator.and_
    OR = operator.or_
    NOT = operator.not_
    XOR = operator.xor

    @staticmethod
    def and_gate(a, b):
        return LogicGateSystem.AND(a, b)

    @staticmethod
    def or_gate(a, b):
        return LogicGateSystem.OR(a, b)

    @staticmethod
    def not_gate(a):
        return LogicGateSystem.NOT(a)

    @staticmethod
    def xor_gate(a, b):
        return LogicGateSystem.XOR(a, b)

if __name__ == '__main__':
    print(f"AND: {LogicGateSystem.and_gate(1, 0)}")
    print(f"OR: {LogicGateSystem.or_gate(1, 0)}")
    print(f"NOT 1: {LogicGateSystem.not_gate(1)}")
    print(f"XOR: {LogicGateSystem.xor_gate(1, 0)}")