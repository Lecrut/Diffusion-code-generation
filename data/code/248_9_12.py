class AdditionCalculator:
    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    calculator = AdditionCalculator()
    print(calculator.add(3, 4))
    print(calculator.add(-1, -2))
    print(calculator.add(0, 0))