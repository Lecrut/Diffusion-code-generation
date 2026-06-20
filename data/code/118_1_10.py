class FigureProduct:
    def __init__(self, figure1: float, figure2: float):
        self.figure1 = figure1
        self.figure2 = figure2

    def calculate(self) -> float:
        return self.figure1 * self.figure2

if __name__ == '__main__':
    num1 = 3.1415926535
    num2 = 2.7182818284
    product = FigureProduct(num1, num2)
    result = product.calculate()
    print(result)