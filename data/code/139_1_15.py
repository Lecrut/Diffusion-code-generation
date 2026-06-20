import operator

class LogicGateSystem:
    AND = operator.and_
    OR = operator.or_
    NOT = operator.not_
    XOR = operator.xor

if __name__ == '__main__':
    gate_system = LogicGateSystem()
    print(f"AND(1, 0): {gate_system.AND(1, 0)}")
    print(f"OR(1, 0): {gate_system.OR(1, 0)}")
    print(f"NOT(1): {gate_system.NOT(1)}")
    print(f"XOR(1, 0): {gate_system.XOR(1, 0)}")