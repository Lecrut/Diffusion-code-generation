import operator

class LogicGateSystem:
    AND = staticmethod(operator.and_)
    OR = staticmethod(operator.or_)
    NOT = staticmethod(operator.not_)
    XOR = staticmethod(operator.xor)
if __name__ == '__main__':
    logic_gate_system = LogicGateSystem()
    print(logic_gate_system.AND(1, 0))
    print(logic_gate_system.OR(1, 0))
    print(logic_gate_system.NOT(1))
    print(logic_gate_system.XOR(1, 0))