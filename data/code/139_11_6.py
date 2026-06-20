class LogicGate:
    def __init__(self, gate_type):
        self.gate_type = gate_type

    def evaluate(self, inputs):
        if self.gate_type == 'AND':
            return all(inputs)
        elif self.gate_type == 'OR':
            return any(inputs)
        elif self.gate_type == 'NOT':
            return not inputs[0]
        else:
            raise ValueError("Invalid gate type")

if __name__ == '__main__':
    and_gate = LogicGate('AND')
    print(f"AND: {and_gate.evaluate([True, False])}")
    or_gate = LogicGate('OR')
    print(f"OR: {or_gate.evaluate([True, False])}")
    not_gate = LogicGate('NOT')
    print(f"NOT (of True): {not_gate.evaluate([True])}")