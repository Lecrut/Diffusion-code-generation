class SafeDifferenceCalculator:
    def __init__(self, a, b):
        self.validate_inputs(a, b)
        self.a = a
        self.b = b
    
    def validate_inputs(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both inputs must be numbers")
    
    def compute_difference(self):
        return max(0, abs(self.a - self.b))

if __name__ == '__main__':
    calculator = SafeDifferenceCalculator(50, 20)
    print(calculator.compute_difference())