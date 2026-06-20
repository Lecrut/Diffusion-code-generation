class MathOperations:
    @staticmethod
    def multiply_figures(a: float, b: float) -> float:
        return a * b

if __name__ == '__main__':
    result = MathOperations.multiply_figures(3.5, 2.0)
    print(result)