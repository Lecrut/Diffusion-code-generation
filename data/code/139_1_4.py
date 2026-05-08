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
    gate = LogicGate(a=1, b=0)
    print(f"AND: {gate.and_()}")
    print(f"OR: {gate.or_()}")
    print(f"NOT A: {gate.not_()}")