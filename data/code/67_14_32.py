def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be either integers or floating-point numbers.')

def compute_sum(a, b):
    validate_numbers(a, b)
    return a + b

class SumOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def execute(self):
        return compute_sum(self.a, self.b)

if __name__ == '__main__':
    operation1 = SumOperation(5, 3)
    print(operation1.execute())
    
    operation2 = SumOperation(2.5, 4.7)
    print(operation2.execute())
    
    operation3 = SumOperation(-1, -1)
    print(operation3.execute())
    
    operation4 = SumOperation(0, 0)
    print(operation4.execute())
    
    operation5 = SumOperation(100, 200.5)
    print(operation5.execute())