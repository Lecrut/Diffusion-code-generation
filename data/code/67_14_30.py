def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be either integers or floating-point numbers.')
    return a + b

class SumOperation:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        try:
            return add_numbers(self.a, self.b)
        except ValueError as e:
            print(f'Error: {e}')
            return None
if __name__ == '__main__':
    operation1 = SumOperation(5, 3)
    result1 = operation1.execute()
    print(result1)
    operation2 = SumOperation(2.5, 4.7)
    result2 = operation2.execute()
    print(result2)
    operation3 = SumOperation('a', 3)
    result3 = operation3.execute()
    print(result3)