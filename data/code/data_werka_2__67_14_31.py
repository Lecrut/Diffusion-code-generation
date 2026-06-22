def compute_sum(a, b):
    return a + b

class SumOperation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def execute(self):
        return compute_sum(self.num1, self.num2)

if __name__ == '__main__':
    operation1 = SumOperation(5, 3)
    print(operation1.execute())
    
    operation2 = SumOperation(2.5, 4.7)
    print(operation2.execute())
    
    operation3 = SumOperation(-10, 20.5)
    print(operation3.execute())
    
    operation4 = SumOperation(0, 0)
    print(operation4.execute())