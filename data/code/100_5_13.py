class AndGate:
    def __init__(self):
        self.gate_type = "AND"

    def process(self, val1, val2):
        if not (isinstance(val1, bool) and isinstance(val2, bool)):
            raise ValueError("Inputs must be booleans")
        return val1 & val2

    def verify(self, val1, val2):
        return self.process(val1, val2)

if __name__ == '__main__':
    gate = AndGate()
    print(gate.verify(True, True))
    print(gate.verify(True, False))
    print(gate.verify(False, True))
    print(gate.verify(False, False))