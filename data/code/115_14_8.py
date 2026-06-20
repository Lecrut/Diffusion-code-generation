class Divider:
    @staticmethod
    def divide(dividend=150.75, divisor=3.0):
        return dividend / divisor if divisor != 0 else 'Division by zero'

if __name__ == '__main__':
    divider = Divider()
    print(divider.divide())