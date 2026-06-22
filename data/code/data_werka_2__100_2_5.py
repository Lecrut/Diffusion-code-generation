class AndGateChecker:
    def __init__(self, name="AND"):
        self.name = name
        self.truth_table = {
            (0, 0, 0): 0,
            (0, 0, 1): 0,
            (0, 1, 0): 0,
            (0, 1, 1): 0,
            (1, 0, 0): 0,
            (1, 0, 1): 0,
            (1, 1, 0): 0,
            (1, 1, 1): 1
        }

    def evaluate(self, a, b, c):
        if a not in (0, 1) or b not in (0, 1) or c not in (0, 1):
            raise ValueError("Inputs must be 0 or 1")
        return a and b and c

    def validate(self, a, b, c, expected):
        result = self.evaluate(a, b, c)
        return result == expected

if __name__ == '__main__':
    gate = AndGateChecker()
    
    inputs = (1, 1, 1)
    expected = 1
    result = gate.evaluate(*inputs)
    valid = gate.validate(*inputs, expected)
    
    print(f"Inputs: {inputs}")
    print(f"Expected: {expected}")
    print(f"Result: {result}")
    print(f"Valid: {valid}")
    
    inputs2 = (1, 0, 1)
    expected2 = 0
    result2 = gate.evaluate(*inputs2)
    valid2 = gate.validate(*inputs2, expected2)
    
    print(f"Inputs: {inputs2}")
    print(f"Expected: {expected2}")
    print(f"Result: {result2}")
    print(f"Valid: {valid2}")