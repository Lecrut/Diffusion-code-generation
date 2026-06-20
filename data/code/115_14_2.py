if __name__ == '__main__':
    dividend = 150.75
    divisor = 3.0
    result = (lambda x, y: x / y if y != 0 else 'Division by zero')(dividend, divisor)
    print(result)