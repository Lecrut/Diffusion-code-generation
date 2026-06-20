class FigureProduct:
    def __init__(self, figure1: float, figure2: float):
        if not all(isinstance(f, (int, float)) for f in [figure1, figure2]):
            raise ValueError("Both figures must be numeric.")
        self.figure1 = figure1
        self.figure2 = figure2

    def calculate(self) -> float:
        return self.figure1 * self.figure2

if __name__ == '__main__':
    product_instance = FigureProduct(3.1415926535, 2.7182818284)
    result = product_instance.calculate()
    print(result)