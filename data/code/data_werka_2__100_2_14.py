class ThreeInputLogicGate:
    def __init__(self, gate_type):
        if gate_type != 'AND':
            raise ValueError("Unsupported gate type")
        self.gate_type = gate_type

    def evaluate(self, inputs):
        if len(inputs) != 3:
            raise ValueError("Exactly three inputs required")
        result = all(inputs)
        return result

    def get_gate_type(self):
        return self.gate_type

if __name__ == '__main__':
    gate = ThreeInputLogicGate('AND')
    print(f"Gate Type: {gate.get_gate_type()}")
    inputs = [True, False, True]
    result = gate.evaluate(inputs)
    print(f"Result for {inputs}: {result}")
    inputs2 = [True, True, True]
    result2 = gate.evaluate(inputs2)
    print(f"Result for {inputs2}: {result2}")