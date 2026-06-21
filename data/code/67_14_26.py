def add_values(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be either integers or floating-point numbers.')
    return a + b

class SumOperation:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    
    def execute(self):
        return add_values(self.value1, self.value2)

if __name__ == '__main__':
    operation1 = SumOperation(5, 3)
    print(operation1.execute())
    
    operation2 = SumOperation(2.5, 4.7)
    print(operation2.execute())
    
    operation3 = SumOperation(-1, -1)
    print(operation3.execute())
    
    operation4 = SumOperation(0, 0)
    print(operation4.execute())