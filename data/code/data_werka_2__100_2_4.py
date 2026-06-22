class LogicGateValidator:
    def __init__(self, gate_type='AND'):
        self.gate_type = gate_type

    def validate_inputs(self, a, b, c):
        if not all(isinstance(x, int) for x in (a, b, c)):
            raise ValueError("Inputs must be integers")
        if not all(x in (0, 1) for x in (a, b, c)):
            raise ValueError("Inputs must be 0 or 1")

    def compute(self, a, b, c):
        self.validate_inputs(a, b, c)
        if self.gate_type == 'AND':
            return 1 if (a == 1 and b == 1 and c == 1) else 0
        raise ValueError(f"Unsupported gate type: {self.gate_type}")

    def check_validity(self, a, b, c, expected):
        self.validate_inputs(a, b, c)
        if expected not in (0, 1):
            raise ValueError("Expected output must be 0 or 1")
        actual = self.compute(a, b, c)
        return actual == expected

if __name__ == '__main__':
    validator = LogicGateValidator('AND')
    result = validator.check_validity(1, 1, 1, 1)
    print(result)