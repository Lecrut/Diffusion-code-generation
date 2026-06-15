class Multiplier:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation
    def multiply(self):
        if self.operation == 'add':
            return self.a + self.b
        elif self.operation == 'subtract':
            return self.a - self.b
        elif self.operation == 'multiply':
            return self.a * self.b
        else:
            raise ValueError("Unsupported operation")
if __name__ == '__main__':
    m1 = Multiplier(10, 5, 'multiply')
    result1 = m1.multiply()
    print(f"10 multiplied by 5 is: {result1}")
    m2 = Multiplier(20, 8, 'add')
    result2 = m2.multiply()
    print(f"20 added to 8 is: {result2}")
    m3 = Multiplier(15, 3, 'subtract')
    result3 = m3.multiply()
    print(f"15 minus 3 is: {result3}")