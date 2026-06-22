class LogicGateValidator:
    def __init__(self, gate_type):
        self.gate_type = gate_type

    def evaluate(self, inputs):
        if self.gate_type != 'AND':
            raise ValueError("Unsupported gate type")
        if len(inputs) != 3:
            raise ValueError("AND gate requires exactly 3 inputs")
        val1 = bool(inputs[0])
        val2 = bool(inputs[1])
        val3 = bool(inputs[2])
        result = val1 and val2 and val3
        return result

    def validate(self, inputs, expected):
        computed = self.evaluate(inputs)
        is_valid = computed == expected
        return computed, is_valid

if __name__ == '__main__':
    gate = LogicGateValidator('AND')
    sample_inputs = (0, 1, 1)
    target_output = 0
    actual_result, validity_status = gate.validate(sample_inputs, target_output)
    print(actual_result)
    print(validity_status)