class AmountCalculator:
    def subtract(self, amount1, amount2):
        return amount1 - amount2
if __name__ == '__main__':
    calculator = AmountCalculator()
    result = calculator.subtract(100, 45)
    print(result)