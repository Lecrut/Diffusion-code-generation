class FactorialCalculator:
    def __init__(self, number):
        self.number = number

    def compute(self):
        result = 1
        for i in range(2, self.number + 1):
            result *= i
        return result

    def get_input(self):
        return self.number

if __name__ == '__main__':
    calculator = FactorialCalculator(20)
    print(calculator.compute())
    print(calculator.get_input())