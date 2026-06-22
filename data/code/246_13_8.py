class DecimalCalculator:
    def __init__(self, decimal1: float, decimal2: float):
        self.decimal1 = decimal1
        self.decimal2 = decimal2
    
    def sum_decimals(self) -> float:
        return self.decimal1 + self.decimal2

if __name__ == '__main__':
    calculator = DecimalCalculator(4.5, 3.2)
    result = calculator.sum_decimals()
    print(result)