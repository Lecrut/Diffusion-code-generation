class LogicGate:
    def __init__(self, gate_type):
        self.gate_type = gate_type

    def evaluate(self, inputs):
        if self.gate_type == 'AND':
            return all(inputs)
        elif self.gate_type == 'OR':
            return any(inputs)
        elif self.gate_type == 'NOT':
            if len(inputs) != 1:
                raise ValueError("NOT gate requires exactly one input")
            return not inputs[0]
        else:
            raise ValueError("Unsupported gate type")

if __name__ == '__main__':
    and_gate = LogicGate('AND')
    or_gate = LogicGate('OR')
    not_gate = LogicGate('NOT')

    print(f"AND: {and_gate.evaluate([True, False])}")
    print(f"OR: {or_gate.evaluate([True, False])}")
    print(f"NOT (of True): {not_gate.evaluate([True])}")