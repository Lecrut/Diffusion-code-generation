class DecimalAdder:
    DECIMAL1 = 3.5
    DECIMAL2 = 2.1

    @staticmethod
    def add_decimals(a, b):
        return a + b

if __name__ == '__main__':
    calculator = DecimalAdder()
    result = calculator.add_decimals(DecimalAdder.DECIMAL1, DecimalAdder.DECIMAL2)
    print(result)