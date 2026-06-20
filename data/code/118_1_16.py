class FigureProduct:
    def __init__(self, figure1: float, figure2: float):
        if not isinstance(figure1, (int, float)) or not isinstance(figure2, (int, float)):
            raise ValueError("Both figures must be numeric")
        self.figure1 = figure1
        self.figure2 = figure2

    def calculate(self) -> float:
        return self.figure1 * self.figure2

if __name__ == '__main__':
    fig1 = 3.1415926535
    fig2 = 2.7182818284
    product = FigureProduct(fig1, fig2)
    print(product.calculate())