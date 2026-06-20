class LogicGate:
    AND = 'and'
    OR = 'or'
    NOT = 'not'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def evaluate(self, gate_type):
        if gate_type == self.AND:
            return self.a and self.b
        elif gate_type == self.OR:
            return self.a or self.b
        elif gate_type == self.NOT:
            return not self.a
        else:
            raise ValueError("Invalid gate type")

if __name__ == '__main__':
    gate = LogicGate(True, False)
    print(f"AND: {gate.evaluate(LogicGate.AND)}")
    print(f"OR: {gate.evaluate(LogicGate.OR)}")
    print(f"NOT (of a): {gate.evaluate(LogicGate.NOT)}")