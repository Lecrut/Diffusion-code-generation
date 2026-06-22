class DecimalOperations:
    @staticmethod
    def add_decimals(a: float, b: float) -> float:
        return a + b

if __name__ == '__main__':
    result = DecimalOperations.add_decimals(3.5, 2.1)
    print(result)