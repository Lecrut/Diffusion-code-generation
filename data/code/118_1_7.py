class FigureProduct:
    def __init__(self, num1: float, num2: float):
        if not all(isinstance(i, (int, float)) for i in [num1, num2]):
            raise ValueError("Both inputs must be numeric figures.")
        self.num1 = num1
        self.num2 = num2

    def calculate(self) -> float:
        return self.num1 * self.num2

if __name__ == '__main__':
    try:
        product = FigureProduct(3.1415926535, 2.7182818284)
        result = product.calculate()
        print(result)
    except ValueError as e:
        print(e)