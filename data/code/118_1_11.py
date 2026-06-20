class FigureProduct:
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def calculate(self) -> float:
        return self.num1 * self.num2

if __name__ == '__main__':
    sample_num1 = 4.5678901234
    sample_num2 = 5.4321098765
    product_instance = FigureProduct(sample_num1, sample_num2)
    result = product_instance.calculate()
    print(result)