class LogicGate:
    def __init__(self, gate_type):
        if gate_type not in ['AND', 'OR', 'NOT']:
            raise ValueError("Invalid gate type")
        self.gate_type = gate_type

    def evaluate(self, a, b=None):
        if self.gate_type == 'AND':
            return a and b
        elif self.gate_type == 'OR':
            return a or b
        else:
            return not a

if __name__ == '__main__':
    and_gate = LogicGate('AND')
    print(f"AND: {and_gate.evaluate(True, False)}")
    
    or_gate = LogicGate('OR')
    print(f"OR: {or_gate.evaluate(False, True)}")

    not_gate = LogicGate('NOT')
    print(f"NOT (of a): {not_gate.evaluate(True)}")