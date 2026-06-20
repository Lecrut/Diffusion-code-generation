import operator

class LogicGateSystem:
    _gates = {
        'AND': operator.and_,
        'OR': operator.or_,
        'NOT': operator.not_,
        'XOR': operator.xor
    }

    @staticmethod
    def apply_gate(gate_name, a, b=None):
        if gate_name == 'NOT':
            return LogicGateSystem._gates[gate_name](a)
        else:
            return LogicGateSystem._gates[gate_name](a, b)

if __name__ == '__main__':
    print(f"AND: {LogicGateSystem.apply_gate('AND', 1, 0)}")
    print(f"OR: {LogicGateSystem.apply_gate('OR', 1, 0)}")
    print(f"NOT a: {LogicGateSystem.apply_gate('NOT', 1)}")
    print(f"XOR: {LogicGateSystem.apply_gate('XOR', 1, 0)}")