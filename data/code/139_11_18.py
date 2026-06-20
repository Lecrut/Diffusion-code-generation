class LogicGate:
    def __init__(self, gate_type):
        self.gate_type = gate_type.lower()

    def validate_input(self, *inputs):
        if not all(isinstance(i, bool) for i in inputs):
            raise ValueError("All inputs must be boolean values")

    def and_gate(self, a, b):
        self.validate_input(a, b)
        return a and b

    def or_gate(self, a, b):
        self.validate_input(a, b)
        return a or b

    def not_gate(self, a):
        self.validate_input(a)
        return not a

if __name__ == '__main__':
    gate = LogicGate('and')
    print(f"AND: {gate.and_gate(True, False)}")
    print(f"OR: {gate.or_gate(False, True)}")
    print(f"NOT (of True): {gate.not_gate(True)}")

    gate2 = LogicGate('or')
    print(f"OR: {gate2.or_gate(True, True)}")