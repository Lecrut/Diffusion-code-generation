class SafeDivider:
    @staticmethod
    def divide(x, y):
        return x / y if y != 0 else 'Division by zero'

if __name__ == '__main__':
    result = SafeDivider.divide(150.75, 3.0)
    print(result)