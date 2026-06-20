class FigureProduct:
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    @staticmethod
    def calculate(num1: float, num2: float) -> float:
        return num1 * num2

if __name__ == '__main__':
    fig_product = FigureProduct(3.1415926535, 2.7182818284)
    result = FigureProduct.calculate(fig_product.num1, fig_product.num2)
    print(result)