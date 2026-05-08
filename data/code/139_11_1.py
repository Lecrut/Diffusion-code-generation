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
    print(f"AND: {gate.and_gate()}")
    print(f"OR: {gate.or_gate()}")
    print(f"NOT (of a): {gate.not_gate()}")
    gate2 = LogicGate(True, True)
    print(f"AND: {gate2.and_gate()}")
    print(f"OR: {gate2.or_gate()}")
    print(f"NOT (of a): {gate2.not_gate()}")