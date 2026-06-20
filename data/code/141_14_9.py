class LogicGates:
    def __init__(self):
        self.inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

    def and_gate(self):
        return [a & b for a, b in self.inputs]

    def or_gate(self):
        return [a | b for a, b in self.inputs]

    def not_gate_a(self):
        return [~a for a, _ in self.inputs]

    def not_gate_b(self):
        return [~b for _, b in self.inputs]

if __name__ == '__main__':
    logic_gates = LogicGates()
    print("A AND B:", logic_gates.and_gate())
    print("A OR B:", logic_gates.or_gate())
    print("NOT A:", logic_gates.not_gate_a())
    print("NOT B:", logic_gates.not_gate_b())