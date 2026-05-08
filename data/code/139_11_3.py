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
    print("AND operation (True and False):", gate.and_gate())
    print("OR operation (True or False):", gate.or_gate())
    print("NOT operation (not True):", gate.not_gate())
    gate2 = LogicGate(True, True)
    print("\nAND operation (True and True):", gate2.and_gate())
    print("OR operation (True or True):", gate2.or_gate())
    print("NOT operation (not True):", gate2.not_gate())