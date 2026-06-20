if __name__ == '__main__':
    dividend = 150.75
    divisor = 3.0

    def divide(x, y):
        if y == 0:
            return 'Division by zero'
        return x / y

    result = divide(dividend, divisor)
    print(result)