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
    print(f"AND (True and False): {gate_and.evaluate(True, False)}")
    
    gate_or = LogicGate('OR')
    print(f"OR (True or False): {gate_or.evaluate(True, False)}")
    
    gate_not = LogicGate('NOT')
    print(f"NOT (not True): {gate_not.evaluate(True)}")