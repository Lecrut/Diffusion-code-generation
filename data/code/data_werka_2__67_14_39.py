def compute_sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be either integers or floating-point numbers.')
    return a + b

class SumOperation:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2
    
    def execute(self):
        return compute_sum(self.operand1, self.operand2)

if __name__ == '__main__':
    operations = [
        SumOperation(5, 3),
        SumOperation(2.5, 4.7),
        SumOperation(-1, -1),
        SumOperation(0, 0),
        SumOperation(100, 200.5)
    ]
    
    for operation in operations:
        result = operation.execute()
        print(f"Sum of {operation.operand1} and {operation.operand2}: {result}")