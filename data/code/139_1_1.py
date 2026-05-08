class LogicGate:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def and_op(self):
        return self.a and self.b
    def or_op(self):
        return self.a or self.b
    def not_op(self):
        return not self.a
if __name__ == '__main__':
    gate = LogicGate(1, 0)
    print(f"AND operation: {gate.and_op()}")
    print(f"OR operation: {gate.or_op()}")
    print(f"NOT operation (of a): {gate.not_op()}")