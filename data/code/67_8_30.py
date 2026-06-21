class SumOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def execute(self):
        if not all(isinstance(i, (int, float)) for i in [self.a, self.b]):
            raise ValueError("Both arguments must be numbers")
        return self.a + self.b

if __name__ == '__main__':
    try:
        operation = SumOperation(15, 25)
        print(operation.execute())
    except ValueError as e:
        print(e)