class LogicGateValidator:
    def __init__(self, name, operation):
        self.name = name
        self.operation = operation

    def validate(self, inputs, expected):
        if not all(isinstance(i, int) for i in inputs):
            raise ValueError("Inputs must be integers")
        if len(inputs) != 3:
            raise ValueError("Exactly three inputs required")
        if expected not in (0, 1):
            raise ValueError("Expected output must be 0 or 1")
        
        actual = self.operation(*inputs)
        is_valid = actual == expected
        return {
            "gate": self.name,
            "inputs": inputs,
            "expected": expected,
            "actual": actual,
            "valid": is_valid
        }

def and_gate(a, b, c):
    return a and b and c

if __name__ == '__main__':
    validator = LogicGateValidator("AND", and_gate)
    result = validator.validate([1, 1, 1], 1)
    print(result)