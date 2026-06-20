import operator

class LogicGateSystem:
    AND = operator.and_
    OR = operator.or_
    NOT = operator.not_
    XOR = operator.xor

if __name__ == '__main__':
    print(f"AND: {LogicGateSystem.AND(1, 0)}")
    print(f"OR: {LogicGateSystem.OR(1, 0)}")
    print(f"NOT: {LogicGateSystem.NOT(1)}")
    print(f"XOR: {LogicGateSystem.XOR(1, 0)}")