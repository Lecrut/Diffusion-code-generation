class FigureProduct:
    def __init__(self, figure1: float, figure2: float):
        self.figure1 = figure1
        self.figure2 = figure2

    @staticmethod
    def calculate(figure1: float, figure2: float) -> float:
        return figure1 * figure2

if __name__ == '__main__':
    product_instance = FigureProduct(3.1415926535, 2.7182818284)
    result = FigureProduct.calculate(product_instance.figure1, product_instance.figure2)
    print(result)