class FigureProduct:
    def __init__(self, figure1, figure2):
        self.figure1 = figure1
        self.figure2 = figure2

    def calculate(self):
        return self.figure1 * self.figure2

if __name__ == '__main__':
    product_instance = FigureProduct(4, 5)
    print(product_instance.calculate())