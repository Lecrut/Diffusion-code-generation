def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be either integers or floating-point numbers.')
    return a + b

class SumOperation:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2
    def execute(self):
        return add_numbers(self.operand1, self.operand2)

if __name__ == '__main__':
    operations = {
        'add_integers': (5, 3),
        'add_floats': (2.5, 4.7),
        'add_negatives': (-1, -1),
        'add_zeros': (0, 0),
        'mixed_types': (100, 200.5)
    }
    
    for key, (op1, op2) in operations.items():
        operation = SumOperation(op1, op2)
        result = operation.execute()
        print(f"Result of {key}: {result}")