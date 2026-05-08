class LogicGate:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def and_gate(self):
        return self.a and self.b
    def or_gate(self):
        return self.a or self.b
    def not_gate(self):
        return not self.a
if __name__ == '__main__':
    gate = LogicGate(True, False)
    print("AND:", gate.and_gate())
    print("OR:", gate.or_gate())
    print("NOT (of a):", gate.not_gate())