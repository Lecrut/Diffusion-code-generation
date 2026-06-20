class DivisionHandler:
    DIVISOR = 3.0

    @staticmethod
    def divide(dividend):
        return dividend / DivisionHandler.DIVISOR if DivisionHandler.DIVISOR != 0 else 'Division by zero'

if __name__ == '__main__':
    divider = DivisionHandler()
    print(divider.divide(150.75))