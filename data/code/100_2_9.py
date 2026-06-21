class LogicGateValidator:
    def __init__(self, gate_type):
        self.gate_type = gate_type

    def evaluate(self, inputs):
        if self.gate_type != 'AND':
            raise ValueError("Unsupported gate type")
        if len(inputs) != 3:
            raise ValueError("AND gate requires exactly 3 inputs")
        
        result = True
        for val in inputs:
            if val not in (0, 1):
                raise ValueError("Inputs must be 0 or 1")
            result = result and bool(val)
            if not result:
                return 0
        return 1

if __name__ == '__main__':
    validator = LogicGateValidator('AND')
    sample_inputs = [1, 1, 0]
    output = validator.evaluate(sample_inputs)
    print(output)