class ArithmeticOperations:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def add(self) -> int:
        return self.num1 + self.num2

    def subtract(self) -> int:
        return self.num1 - self.num2

if __name__ == '__main__':
    sample_value_1 = 7
    sample_value_2 = 3
    
    operations = ArithmeticOperations(sample_value_1, sample_value_2)
    print("Addition result:", operations.add())
    print("Subtraction result:", operations.subtract())