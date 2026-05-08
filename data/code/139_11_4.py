class LogicGate:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def and_(self):
        return self.a and self.b
    def or_(self):
        return self.a or self.b
    def not_(self):
        return not self.a
if __name__ == '__main__':
    gate = LogicGate(True, False)
    print(f"AND: {gate.and_()}")
    print(f"OR: {gate.or_()}")
    print(f"NOT of A: {gate.not_()}")
    gate2 = LogicGate(True, True)
    print(f"AND: {gate2.and_()}")
    print(f"OR: {gate2.or_()}")
    print(f"NOT of A: {gate2.not_()}")