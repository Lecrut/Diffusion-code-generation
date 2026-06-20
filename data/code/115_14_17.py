class Divider:
    DIVISOR = 3.0

    @staticmethod
    def divide(x):
        return x / Divider.DIVISOR if Divider.DIVISOR != 0 else 'Division by zero'

if __name__ == '__main__':
    divider = Divider()
    print(divider.divide(150.75))