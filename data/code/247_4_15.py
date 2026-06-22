class LargeIntegerCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def sum_integers(self):
        return self.a + self.b

if __name__ == '__main__':
    calculator = LargeIntegerCalculator(12345678901234567890, 98765432109876543210)
    result = calculator.sum_integers()
    print(result)