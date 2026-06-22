class AdditionCalculator:
    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    calculator = AdditionCalculator()
    result1 = calculator.add(5, 3)
    result2 = calculator.add(-10, 5)
    print(result1)
    print(result2)