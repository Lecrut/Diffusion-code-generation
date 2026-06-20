class LogicGate:
    def __init__(self, gate_type):
        self.gate_type = gate_type

    def evaluate(self, a, b=None):
        if self.gate_type == 'and':
            return a and (b if b is not None else True)
        elif self.gate_type == 'or':
            return a or (b if b is not None else False)
        elif self.gate_type == 'not':
            return not a
        else:
            raise ValueError("Invalid gate type")

if __name__ == '__main__':
    and_gate = LogicGate('and')
    print(f"AND: {and_gate.evaluate(True, False)}")
    
    or_gate = LogicGate('or')
    print(f"OR: {or_gate.evaluate(False, True)}")
    
    not_gate = LogicGate('not')
    print(f"NOT (of True): {not_gate.evaluate(True)}")