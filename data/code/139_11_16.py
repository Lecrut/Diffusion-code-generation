class LogicGate:
    def __init__(self, gate_type):
        self.gate_type = gate_type

    def evaluate(self, a, b=None):
        if self.gate_type == 'AND':
            return a and b
        elif self.gate_type == 'OR':
            return a or b
        elif self.gate_type == 'NOT':
            return not a
        else:
            raise ValueError("Invalid gate type")

if __name__ == '__main__':
    gate_and = LogicGate('AND')
    print(f"AND: {gate_and.evaluate(True, False)}")
    
    gate_or = LogicGate('OR')
    print(f"OR: {gate_or.evaluate(False, True)}")
    
    gate_not = LogicGate('NOT')
    print(f"NOT (of False): {gate_not.evaluate(False)}")