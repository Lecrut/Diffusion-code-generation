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
    gates = {
        'and': LogicGate('AND'),
        'or': LogicGate('OR'),
        'not': LogicGate('NOT')
    }
    
    print(f"AND (True, False): {gates['and'].evaluate(True, False)}")
    print(f"OR (True, False): {gates['or'].evaluate(True, False)}")
    print(f"NOT (True): {gates['not'].evaluate(True)}")